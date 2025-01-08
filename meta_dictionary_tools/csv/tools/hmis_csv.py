import requests
from dataclasses import dataclass
from pathlib import Path
from glob import glob
from zipfile import ZipFile
from io import BytesIO
import polars as pl
from rich import print
import psycopg2


from meta_dictionary_tools import HMIS_SAMPLE_DATA_URL
from meta_dictionary_tools.csv.models import JoinDefinition
from meta_dictionary_tools.data import ALL_CSV_NAMES, FIELD_LOOKUP
from meta_dictionary_tools.data_checks import all_csvs_exist


class Database:
    pass


@dataclass
class PostgresDatabaseConfig(Database):
    """
    Postgres Database Configuration.

    Args:
        username (str): Database username.
        password (str): Database password.
        db_name (str): Database name.
        schema (str, optional): Database schema. Defaults to "hmis_csv".
        db_type (str, optional): Database type. Defaults to "postgresql".
        port (int, optional): Database port. Defaults to 5432.
        server (str, optional): Database server. Defaults to "localhost".
        uri (str, optional): Database URI. Defaults to None.

    Returns:
        None

    """

    username: str
    password: str
    db_name: str
    schema: str = "hmis_csv"
    # TODO: Change to an enum.
    db_type = "postgresql"
    port: int = 5432
    server: str = "localhost"

    def uri(self):
        return f"{self.db_type}://{self.username}:{self.password}@{self.server}:{self.port}/{self.db_name}"


class HMIS_DBLoader:
    """
    Load CSVs into a database.

    Args:
        csv_export_dir (str): Directory where the CSVs are stored.
        db_config (PostgresDatabaseConfig): Database configuration.

    Returns:
        None
    """

    def __init__(self, csv_export_dir: str, db_config: PostgresDatabaseConfig) -> None:

        self.csv_export_dir = csv_export_dir
        self.csv_files = glob(f"{csv_export_dir}/*.csv")
        self.db_config = db_config

        all_csvs_exist(self.csv_files)

        with psycopg2.connect(self.db_config.uri()) as conn:
            with conn.cursor() as cur:
                cur.execute(f"CREATE SCHEMA IF NOT EXISTS {self.db_config.schema};")

    def load_csvs(
        self,
    ) -> None:
        """
        Load CSVs into the database.

        Returns:
            None
        """

        for csv_file in self.csv_files:
            table_name = Path(csv_file).stem
            print(
                f"Loading [purple]{self.db_config.schema}.{table_name}[/purple] into the database."
            )
            self.load_csv(csv_file, table_name)

    def load_csv(self, csv_file: str, table_name: str) -> None:
        """
        Load a single CSV into the database.

        Args:
            csv_file (str): Path to the CSV file.
            table_name (str): Name of the table to create in the database.

        Returns:
            None
        """
        df = pl.read_csv(csv_file)
        table_name = f'{self.db_config.schema}."{table_name}"'

        df.write_database(
            connection=self.db_config.uri(),
            table_name=table_name,
            if_table_exists="replace",
        )


class CSVTools:

    @staticmethod
    def create_missing_csvs(csv_export_dir: str) -> None:
        """
        Create empty csv files in the csv_export_dir for any missing csv files.
        Each CSV shell will contain the appropriate columns, but no data.

        Args:
            csv_export_dir (str): Directory where the csv files are stored.

        Returns:
            None
        """
        if not Path(csv_export_dir).exists():
            raise Exception(f"Directory '{csv_export_dir}' does not exist")

        csv_files = glob(f"{csv_export_dir}/*.csv")

        if not csv_files:
            raise Exception(f"No CSV files found in '{csv_export_dir}'")

        for csv_name in ALL_CSV_NAMES:
            if csv_name not in csv_files:
                with open(f"{csv_export_dir}/{csv_name}.csv", "w") as f:
                    fields = FIELD_LOOKUP[csv_name]
                    print(f"Missing CSV. Creating [purple]'{csv_name}.csv[/purple]'")
                    f.write(",".join(fields) + "\n")

    @staticmethod
    def retrieve_sample_data(
        download_directory: str, download_url: str | None = None
    ) -> None:
        """
        Download the sample data from the HMIS Sample Data repository.

        Args:
            download_directory (str): Directory to save the sample data.
            download_url (str, optional): URL to download the sample data from. Defaults to None.

        Returns:
            None
        """

        if not download_url:
            download_url = HMIS_SAMPLE_DATA_URL

        export_path = Path(download_directory)
        if not export_path.exists():
            export_path.mkdir()

        response = requests.get(download_url)

        if response.status_code == 200:
            zipfile_buffer = ZipFile(BytesIO(response.content))
            zipfile_buffer.extractall(download_directory)
            print(f"Sample data downloaded to '{download_directory}'")
        else:
            raise Exception(
                f"Failed to download sample data from '{HMIS_SAMPLE_DATA_URL}'"
            )


class HMIS_CSVLoader:

    def __init__(self, csv_export_dir: str):
        self.csv_export_dir = csv_export_dir
        self.csv_files = glob(f"{csv_export_dir}/*.csv")

        CSVTools.create_missing_csvs(csv_export_dir)

    def load_csvs(self):
        """
        Load all the CSVs into memory.

        Returns:
            None

        CSVs loaded into memory:
            'Affiliation',
            'Assessment',
            'AssessmentQuestions',
            'AssessmentResults',
            'CEParticipation',
            'Client',
            'CurrentLivingSituation',
            'Disabilities',
            'EmploymentEducation',
            'Enrollment',
            'Event',
            'Exit',
            'Export',
            'Funder',
            'HMISParticipation',
            'HealthAndDV',
            'IncomeBenefits',
            'Inventory',
            'Organization',
            'Project',
            'ProjectCoC',
            'Services',
            'User',
            'YouthEducationStatus'
        """

        self.csvs = {}
        for csv in ALL_CSV_NAMES:
            csv_path = f"{self.csv_export_dir}/{csv}.csv"
            self.csvs[csv] = pl.read_csv(csv_path)

    def prepend_csv_name_to_column_name(self) -> dict:
        """
        Prepend the CSV name to the column name.

        Returns:
            None
        """

        new_csvs = {}
        for csv_name, df in self.csvs.items():
            new_csvs[csv_name] = df.rename(
                {col: f"{csv_name}_{col}" for col in df.columns},
            )

        return new_csvs


class HMIS_CSVDecoder:
    """
    Convert all encoded values in the HMIS CSV sets, into a human
    readable counterpart.
    """

    pass


class OneBigCSV:
    """
    Join all of the HMIS CSV appropriately, into one big CSV.
    """

    @staticmethod
    def load(
        csv_loader: HMIS_CSVLoader, csvs_to_exclude: list[str] | None = None
    ) -> pl.DataFrame:

        csv_loader.load_csvs()
        csv_loader.csvs = csv_loader.prepend_csv_name_to_column_name()

        join_keys = [
            # Enrollments
            JoinDefinition(
                "Client", "Enrollment", "Client_PersonalID", "Enrollment_PersonalID"
            ),
            # Exits
            # JoinDefinition("Client", "Exit", "Client_PersonalID", "Exit_PersonalID"),
            # Projects
            JoinDefinition(
                "Enrollment", "Project", "Enrollment_ProjectID", "Project_ProjectID"
            ),
            # Organizations
            JoinDefinition(
                "Project",
                "Organization",
                "Project_OrganizationID",
                "Organization_OrganizationID",
            ),
            # Funder
            JoinDefinition(
                "Project", "Funder", "Project_ProjectID", "Funder_ProjectID"
            ),
            # Events
            JoinDefinition(
                "Enrollment", "Event", "Enrollment_EnrollmentID", "Event_EnrollmentID"
            ),
            # Current Living Situation
            JoinDefinition(
                "Enrollment",
                "CurrentLivingSituation",
                "Enrollment_EnrollmentID",
                "CurrentLivingSituation_EnrollmentID",
            ),
            # Disabilities
            JoinDefinition(
                "Enrollment",
                "Disabilities",
                "Enrollment_EnrollmentID",
                "Disabilities_EnrollmentID",
            ),
            # Income Benefits
            JoinDefinition(
                "Enrollment",
                "IncomeBenefits",
                "Enrollment_EnrollmentID",
                "IncomeBenefits_EnrollmentID",
            ),
            # HealthAndDV
            JoinDefinition(
                "Enrollment",
                "HealthAndDV",
                "Enrollment_EnrollmentID",
                "HealthAndDV_EnrollmentID",
            ),
            # 'YouthEducationStatus'
            JoinDefinition(
                "Enrollment",
                "YouthEducationStatus",
                "Enrollment_EnrollmentID",
                "YouthEducationStatus_EnrollmentID",
            ),
            # Assessments
            JoinDefinition(
                "Client", "Assessment", "Client_PersonalID", "Assessment_PersonalID"
            ),
            # Assessment Results
            JoinDefinition(
                "Assessment",
                "AssessmentResults",
                "Assessment_AssessmentID",
                "AssessmentResults_AssessmentID",
            ),
            # Assessment Questions
            JoinDefinition(
                "Assessment",
                "AssessmentQuestions",
                "Assessment_AssessmentID",
                "AssessmentQuestions_AssessmentID",
            ),
            # Assessment Results
            JoinDefinition(
                "Assessment",
                "AssessmentResults",
                "Assessment_AssessmentID",
                "AssessmentResults_AssessmentID",
            ),
            # CE Participation
            JoinDefinition(
                "Project",
                "CEParticipation",
                "Project_ProjectID",
                "CEParticipation_ProjectID",
            ),
            # HMIS Participation
            JoinDefinition(
                "Project",
                "HMISParticipation",
                "Project_ProjectID",
                "HMISParticipation_ProjectID",
            ),
            # Inventory
            JoinDefinition(
                "Project",
                "Inventory",
                "Project_ProjectID",
                "Inventory_ProjectID",
            ),
            # Services
            JoinDefinition(
                "Enrollment",
                "Services",
                "Enrollment_EnrollmentID",
                "Services_EnrollmentID",
            ),
            # EmploymentEducation
            JoinDefinition(
                "Enrollment",
                "EmploymentEducation",
                "Enrollment_EnrollmentID",
                "EmploymentEducation_EnrollmentID",
            ),
            # Affiliation
            JoinDefinition(
                "Project", "Affiliation", "Project_ProjectID", "Affiliation_ProjectID"
            ),
        ]

        if csvs_to_exclude:
            join_keys = [
                join_key
                for join_key in join_keys
                if join_key.right_csv_name not in csvs_to_exclude
            ]

        df: pl.DataFrame = csv_loader.csvs["Client"]
        for join_key in join_keys:
            right_df = csv_loader.csvs[join_key.right_csv_name]

            df = df.join(
                right_df,
                left_on=join_key.left_on,
                right_on=join_key.right_on,
                how="full",
            )
        """
            TODO 'User',
        """

        return df.write_csv("one_big_file.csv")

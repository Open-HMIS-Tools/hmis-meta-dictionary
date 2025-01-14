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
from meta_dictionary_tools.data import ALL_CSV_NAMES, ALL_LSA_CSV_NAMES, FIELD_LOOKUP
from meta_dictionary_tools.data_checks import all_csvs_exist


class LSA_HMIS_CSVLoader:

    def __init__(self, csv_export_dir: str):
        self.csv_export_dir = csv_export_dir
        self.csv_files = glob(f"{csv_export_dir}/*.csv")

        # TODO: When loading empty shell files the datatypes are not set.
        # causing the join to fail. Need to fix this.
        LSA_CSVTools.create_missing_csvs(csv_export_dir)

    def load_csvs(self):
        self.csvs = {}
        for csv in ALL_LSA_CSV_NAMES:
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


class LSA_CSVTools:

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

        csv_files = [Path(csv_file).stem for csv_file in csv_files]

        for csv_name in ALL_LSA_CSV_NAMES:
            if csv_name not in csv_files:
                with open(f"{csv_export_dir}/{csv_name}.csv", "w") as f:
                    fields = FIELD_LOOKUP[csv_name]
                    print(f"Missing CSV. Creating [purple]'{csv_name}.csv[/purple]'")
                    f.write(",".join(fields) + "\n")

    # @staticmethod
    # def retrieve_sample_data(
    #     download_directory: str, download_url: str | None = None
    # ) -> None:
    #     """
    #     Download the sample data from the HMIS Sample Data repository.

    #     Args:
    #         download_directory (str): Directory to save the sample data.
    #         download_url (str, optional): URL to download the sample data from. Defaults to None.

    #     Returns:
    #         None
    #     """

    #     if not download_url:
    #         download_url = HMIS_SAMPLE_DATA_URL

    #     export_path = Path(download_directory)
    #     if not export_path.exists():
    #         export_path.mkdir()

    #     response = requests.get(download_url)

    #     if response.status_code == 200:
    #         zipfile_buffer = ZipFile(BytesIO(response.content))
    #         zipfile_buffer.extractall(download_directory)
    #         print(f"Sample data downloaded to '{download_directory}'")
    #     else:
    #         raise Exception(
    #             f"Failed to download sample data from '{HMIS_SAMPLE_DATA_URL}'"
    #         )


class OneBigLSACSV:
    """
    Join all of the HMIS CSV appropriately, into one big CSV.
        "Affiliation.csv",
        "Funder.csv",
        "HMISParticipation.csv",
        "Inventory.csv",
        "LSACalculated.csv",
        "LSAExit.csv",
        "LSAHousehold.csv",
        "LSAPerson.csv",
        "LSAReport.csv",
        "Organization.csv",
        "Project.csv",
        "ProjectCoC.csv"
    """

    @staticmethod
    def load(
        csv_loader: LSA_HMIS_CSVLoader,
        csvs_to_exclude: list[str] | None = None,
    ) -> pl.DataFrame:

        csv_loader.load_csvs()
        csv_loader.csvs = csv_loader.prepend_csv_name_to_column_name()

        df: pl.DataFrame = csv_loader.csvs["Project"]
        join_keys = [
            # ProjectCoC
            JoinDefinition(
                "Project",
                "ProjectCoC",
                "Project_ProjectID",
                "ProjectCoC_ProjectID",
            ),
            # Organization
            JoinDefinition(
                "Project",
                "Organization",
                "Project_OrganizationID",
                "Organization_OrganizationID",
            ),
            # Funder
            JoinDefinition(
                "Project",
                "Funder",
                "Project_ProjectID",
                "Funder_ProjectID",
            ),
            # HMISParticipation
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
        ]

        if csvs_to_exclude:
            join_keys = [
                join_key
                for join_key in join_keys
                if join_key.right_csv_name not in csvs_to_exclude
            ]

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

        return df

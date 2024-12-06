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
        csv_files = glob(f"{csv_export_dir}/*.csv")
        csv_files = [Path(csv_file).stem for csv_file in csv_files]

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

    pass

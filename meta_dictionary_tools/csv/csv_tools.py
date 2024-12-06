import requests
from dataclasses import dataclass
from pathlib import Path
from glob import glob
from zipfile import ZipFile
from io import BytesIO
import polars as pl
from rich import print

from meta_dictionary_tools import HMIS_SAMPLE_DATA_URL
from meta_dictionary_tools.data import ALL_CSV_NAMES
from meta_dictionary_tools.data.models import FIELD_LOOKUP
from meta_dictionary_tools.data_checks import all_csvs_exist


@dataclass
class DatabaseConfig:
    username: str
    password: str
    db_name: str
    db_type = "postgresql"
    port: int = 5432
    server: str = "localhost"
    uri: str = None

    def __post_init__(self):
        self.uri = f"{self.db_type}://{self.username}:{self.password}@{self.server}:{self.port}/{self.db_name}"


class CSVExportLoader:
    """
    WILO: Load CSVs into a database. I'll probably need to ensure the datatypes
         are correct.
    """

    def __init__(self, csv_export_dir: str, db_config: DatabaseConfig) -> None:

        self.csv_export_dir = csv_export_dir
        self.csv_files = glob(f"{csv_export_dir}/*.csv")

        all_csvs_exist(self.csv_files)

        query = """SELECT * FROM lsa_raw_hmis_csv."Affiliation" """
        print(pl.read_database_uri(query=query, uri=db_config.uri))


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

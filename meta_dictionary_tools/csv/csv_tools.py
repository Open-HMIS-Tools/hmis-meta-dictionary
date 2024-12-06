from pathlib import Path
from glob import glob
import requests
from zipfile import ZipFile
from io import BytesIO
import polars as pl
from glob import glob
from rich import print

from meta_dictionary_tools import HMIS_SAMPLE_DATA_URL
from meta_dictionary_tools.data import ALL_CSV_NAMES
from meta_dictionary_tools.data.models import FIELD_LOOKUP
from meta_dictionary_tools.data_checks import all_csvs_exist


class CSVExportLoader:

    def __init__(self, csv_export_dir: str):
        self.csv_export_dir = csv_export_dir
        self.csv_files = glob(f"{csv_export_dir}/*.csv")

        all_csvs_exist(self.csv_files)


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

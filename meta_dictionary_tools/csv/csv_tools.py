from pathlib import Path
from glob import glob
import requests
from zipfile import ZipFile
from io import BytesIO
import polars as pl
from glob import glob


from meta_dictionary_tools import HMIS_SAMPLE_DATA_URL
from meta_dictionary_tools.data import ALL_CSV_NAMES
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
        """

        csv_files = glob(f"{csv_export_dir}/*.csv")
        csv_files = [Path(csv_file).stem for csv_file in csv_files]

        for csv_name in ALL_CSV_NAMES:
            if csv_name not in csv_files:
                with open(f"{csv_export_dir}/{csv_name}.csv", "w") as f:
                    pass

    @staticmethod
    def retrieve_sample_data(
        download_directory: str, download_url: str | None = None
    ) -> None:

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

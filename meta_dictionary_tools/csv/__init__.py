from meta_dictionary_tools.data_checks import all_csvs_exist
from .sample_csv_downloader import RetrieveSampleData


import polars as pl
from glob import glob
from ..data import ALL_CSV_NAMES


class CSVExportLoader:

    def __init__(self, csv_export_dir: str):
        self.csv_export_dir = csv_export_dir
        self.csv_files = glob(f"{csv_export_dir}/*.csv")

        all_csvs_exist(self.csv_files)

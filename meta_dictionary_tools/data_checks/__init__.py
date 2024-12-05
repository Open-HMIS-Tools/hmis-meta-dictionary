from glob import glob
from pathlib import Path
from meta_dictionary_tools.data import ALL_CSV_NAMES


def all_csvs_exist(csv_name_list: list[str]) -> None:
    csv_name_list = [Path(csv_name).stem for csv_name in csv_name_list]
    for csv_name in ALL_CSV_NAMES:
        if csv_name.replace(".csv", "") not in csv_name_list:
            raise Exception(f"Missing CSV: {csv_name}.csv")

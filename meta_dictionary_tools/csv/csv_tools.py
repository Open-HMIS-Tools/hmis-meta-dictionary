from pathlib import Path
from glob import glob
from meta_dictionary_tools.data import ALL_CSV_NAMES


def create_missing_csv_shells(csv_export_dir: str) -> None:
    """
    Create empty csv files in the csv_export_dir for any missing csv files.
    """

    csv_files = glob(f"{csv_export_dir}/*.csv")
    csv_files = [Path(csv_file).stem for csv_file in csv_files]

    for csv_name in ALL_CSV_NAMES:
        if csv_name not in csv_files:
            with open(f"{csv_export_dir}/{csv_name}.csv", "w") as f:
                f.write("")

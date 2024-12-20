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
        # CSVTools.create_missing_lsa_csvs(csv_export_dir)

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
                "Project", "Funder", "Project_ProjectID", "Funder_ProjectID"
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

        return df.write_csv("one_big_file.csv")

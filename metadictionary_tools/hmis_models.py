from dataclasses import dataclass
from pathlib import Path
import os
import pandas as pd


@dataclass
class HMISField:

    csv: str
    element_num: str | None = None
    name: str | None = None
    key_type: str | None = None
    type: str | None = None
    list: str | None = None
    null: str | None = None
    notes: str | None = None
    validate: str | None = None
    field_to_csv_relationship: str | None = None
    relationship_desc: str | None = None

    """
        Allows us to rename entities. E.g., FK fields have the name parsed
        to provide the foreign table name, unfortunately, not all table naming
        follows the fieldNameID, leading to the need for these aliases.
    """
    _csv_aliases = {"Personal": "Client", "Household": "Client"}

    def is_primary_key(self) -> bool:
        return self.key_type == "pk"

    def is_foreign_key(self) -> bool:
        return self.key_type == "fk"

    def is_nullable(self) -> bool:
        return self.null == "Y"

    def get_fk_table_name(self):
        potential_name = self.name.replace("ID", "")

        if potential_name in self._csv_aliases.keys():
            potential_name = self._csv_aliases[potential_name]

        return potential_name

    def __post_init__(self):
        self.name = self.name.strip()


class HMISFields:

    @classmethod
    def load(cls) -> list[HMISField]:

        HMIS_DATA_DICTIONARY_PATH = Path(os.path.dirname(__file__)) / Path(
            "data/hmis_data_dictionary.csv"
        )

        df = pd.read_csv(HMIS_DATA_DICTIONARY_PATH)

        fields = []

        for _, row in df.iterrows():
            field = HMISField(**row)
            fields.append(field)

        return fields

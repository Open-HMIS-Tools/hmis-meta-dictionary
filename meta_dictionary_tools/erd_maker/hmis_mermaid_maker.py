from .hmis_models import HMISField

from rich import print


class FocusedERD:
    def __init__(
        self,
        name: str,
        hmis_fields: list[HMISField],
        exclude_csvs: list[str] | None = None,
    ):
        self.name = name
        self.fields = hmis_fields
        self._csvs = set([field.csv for field in hmis_fields])
        self._exclude_csvs = exclude_csvs

    def generate(self):
        erd_string = "erDiagram\n"

        for csv in self._csvs:

            if csv in self._exclude_csvs:
                continue

            erd_string += self.create_table(csv)

        erd_string += self.get_foreign_key_relationships()

        return erd_string

    def get_foreign_key_relationships(self):
        diagram_string = ""

        for field in self.fields:
            if not field.is_foreign_key():
                continue

            if field.get_fk_table_name() in self._exclude_csvs:
                continue

            diagram_string += (
                f"    {field.csv} ||--|| {field.get_fk_table_name()} : {field.name}\n"
            )

        return diagram_string

    def create_table(self, table_name: str):

        fields = [field for field in self.fields if field.csv == table_name]

        table_string = f"    {table_name} {{\n"

        for field in fields:
            table_string += f"         {field.type} {field.name}\n"

        table_string += "    }\n"

        return table_string

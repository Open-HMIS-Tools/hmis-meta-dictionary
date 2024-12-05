from .hmis_models import HMISField


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
                print("true")
                continue

            diagram_string += (
                f"    {field.csv} ||--|| {field.get_fk_table_name()} : {field.name}\n"
            )

        return diagram_string

    def create_table(self, table_name: str):

        fields = [field for field in self.fields if field.csv == table_name]

        table_string = f"    {table_name} {{\n"

        for field in fields:
            table_string += f"         {field.type} {field.name} {'?' if field.is_nullable() else ''}\n"

        table_string += "    }\n"

        return table_string


class FocusedERDWriter:

    def __init__(self, erds: list[FocusedERD]):
        self.erds = erds

    def write(self, output_path: str) -> None:

        for erd in self.erds:
            erd_str = erd.generate()
            print(erd_str)

import pandas as pd
import os
from meta_dictionary_tools.data import ALL_CSV_NAMES
import re
from stringcase import snakecase

INPUT_PATH = "meta_dictionary_tools/data/hmis_data_dictionary.csv"
OUTPUT_DIR = "meta_dictionary_tools/data"
df = pd.read_csv(INPUT_PATH)


"""
Generate field name lists for each CSV file
"""
os.system(f"rm -f {OUTPUT_DIR}/models.py")

lookup_str = "{\n"

for csv in ALL_CSV_NAMES:
    sub_df = df[df["csv"] == csv]
    fields = sub_df["name"].to_list()

    field_name = f"{csv.upper()}_FIELDS"
    lookup_str += f'"{csv}": {field_name},\n'

    with open(f"{OUTPUT_DIR}/models.py", "+a") as f:
        f.write(f'{field_name} = [\n\t"')
        f.write('",\n\t"'.join(fields))
        f.write('"\n]\n\n')


with open(f"{OUTPUT_DIR}/models.py", "+a") as f:
    lookup_str += "}"
    f.write(f"FIELD_LOOKUP = {lookup_str}\n")

"""
1. Load CSVs
2. Check headers for each CSV
3. Create a table for each CSV
4. Ensure correct data type.
"""

import os
from meta_dictionary_tools.csv.tools.hmis_csv import (
    HMIS_DBLoader,
    CSVTools,
    PostgresDatabaseConfig,
)

OUTPUT_DIR = "data/hmis_csv_sample_data"

# Get rid of old data. We need fresh every time! 🍒
os.system(f"rm -rf {OUTPUT_DIR}")

"""
Download sample data from LSA Sample Code repository
    https://github.com/HMIS/LSASampleCode
"""
CSVTools.retrieve_sample_data(download_directory=OUTPUT_DIR)

# Ensure all CSVs exist
CSVTools.create_missing_csvs(csv_export_dir=OUTPUT_DIR)

csv_export_loader = HMIS_DBLoader(
    csv_export_dir=OUTPUT_DIR,
    db_config=PostgresDatabaseConfig(
        db_name="analytics",
        username="ladvien",
        password="",
        server="localhost",
        port=5432,
    ),
)


csv_export_loader.load_csvs()

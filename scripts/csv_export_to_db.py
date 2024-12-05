"""
1. Load CSVs
2. Check headers for each CSV
3. Create a table for each CSV
4. Ensure correct data type.
"""

from meta_dictionary_tools.csv_loader import RetrieveSampleData, CSVExportLoader

OUTPUT_DIR = "data/hmis_csv_sample_data"
RetrieveSampleData(download_directory=OUTPUT_DIR)

csv_export_loader = CSVExportLoader(csv_export_dir=OUTPUT_DIR)

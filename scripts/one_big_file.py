from meta_dictionary_tools.csv.csv_tools import HMIS_CSVLoader, OneBigCSV

OUTPUT_DIR = "data/hmis_csv_sample_data"

csvs_to_exclude = ["Services"]

csv_loader = HMIS_CSVLoader(OUTPUT_DIR)
df = OneBigCSV.load(csv_loader, csvs_to_exclude)

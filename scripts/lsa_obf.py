from meta_dictionary_tools.csv.tools import LSA_HMIS_CSVLoader, OneBigLSACSV


OUTPUT_DIR = "/home/ladvien/tmp/<COC>"

csvs_to_exclude = ["Services"]

csv_loader = LSA_HMIS_CSVLoader(OUTPUT_DIR)
df = OneBigLSACSV.load(csv_loader, csvs_to_exclude)

print(df)
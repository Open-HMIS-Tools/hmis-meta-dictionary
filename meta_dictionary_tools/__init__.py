import os
from pathlib import Path

HMIS_DATA_DICTIONARY_PATH = Path(os.path.dirname(__file__)) / Path(
    "data/hmis_data_dictionary.csv"
)

HMIS_SAMPLE_DATA_URL = "https://github.com/HMIS/LSASampleCode/raw/refs/heads/master/Sample%20Data/Sample%20HMIS%20Data.zip"

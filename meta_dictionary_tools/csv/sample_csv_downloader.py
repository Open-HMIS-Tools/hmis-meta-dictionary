from pathlib import Path
import requests
from zipfile import ZipFile
from io import BytesIO

HMIS_SAMPLE_DATA_URL = "https://github.com/HMIS/LSASampleCode/raw/refs/heads/master/Sample%20Data/Sample%20HMIS%20Data.zip"


class RetrieveSampleData:

    def __init__(
        self, download_directory: str, download_url: str | None = None
    ) -> None:
        self.download_directory = download_directory

        if not download_url:
            self.download_url = HMIS_SAMPLE_DATA_URL

        export_path = Path(download_directory)
        if not export_path.exists():
            export_path.mkdir()

        response = requests.get(self.download_url)

        if response.status_code == 200:
            zipfile_buffer = ZipFile(BytesIO(response.content))
            zipfile_buffer.extractall(download_directory)
            print(f"Sample data downloaded to '{download_directory}'")
        else:
            raise Exception(
                f"Failed to download sample data from '{HMIS_SAMPLE_DATA_URL}'"
            )

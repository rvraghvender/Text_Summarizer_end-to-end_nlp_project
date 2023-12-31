import os
import urllib.request as request
import zipfile
from pathlib import Path
from text_summarizer.logging.logger import logging
from text_summarizer.utils.common import get_size
from text_summarizer.entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig) -> None:
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            file_name, headers = request.urlretrieve(
                url = self.config.source_url,
                filename = self.config.local_data_file
            )
            logging.info(f'{file_name} download! with the following info: \n{headers}')
        else:
            logging.info(f'File already exists of size: {get_size(Path(self.config.local_data_file))}')
    
    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory.
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
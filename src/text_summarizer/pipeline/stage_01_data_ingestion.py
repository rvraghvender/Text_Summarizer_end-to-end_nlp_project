from text_summarizer.config.configuration import ConfigurationManager
from text_summarizer.components.data_ingestion import DataIngestion
from text_summarizer.logging.exception import CustomException
from text_summarizer.logging.logger import logging
import sys


class DataIngestionTrainingPipeline:
    def __init__(self) -> None:
        pass
        
    def main(self):
        try:
            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(config=data_ingestion_config)
            data_ingestion.download_file()
            data_ingestion.extract_zip_file()
        except Exception as e:
            logging.exception(e)
            raise CustomException(e, sys)
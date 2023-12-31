from text_summarizer.config.configuration import ConfigurationManager
from text_summarizer.components.data_validation import DataValidation


class DataValidationTrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            data_validation_config = config.get_data_validation_config()
            data_validation = DataValidation(config=data_validation_config)
            data_validation.validate_all_file_exist()
        except Exception as e:
            raise e
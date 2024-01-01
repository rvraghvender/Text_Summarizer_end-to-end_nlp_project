from text_summarizer.config.configuration import ConfigurationManager
from text_summarizer.components.model_evaluation import ModelEvaluation

class ModelEvaluationTrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            model_evaluation_config = config.get_model_evaluation_config()
            model_evaluation = ModelEvaluation(config=model_evaluation_config)
            model_evaluation.evaluate()
        except Exception as e:
            raise e
        
if __name__ == '__main__':
    try:
        obj = ModelEvaluationTrainingPipeline()
        obj.main()
    except Exception as e:
        raise e
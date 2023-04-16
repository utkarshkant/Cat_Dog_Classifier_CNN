# imports
from CAT_DOG_CLASSIFIER_CNN.config import ConfigurationManager
from CAT_DOG_CLASSIFIER_CNN.components import DataIngestion
from CAT_DOG_CLASSIFIER_CNN import logger

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    # def main(self):
    def main():
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.unzip_and_clean()

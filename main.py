from CAT_DOG_CLASSIFIER_CNN.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from CAT_DOG_CLASSIFIER_CNN import logger

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>> Stage {STAGE_NAME} started <<<<<")
    data_ingestion = DataIngestionTrainingPipeline
    data_ingestion.main()
    logger.info(f">>>>> Stage {STAGE_NAME} completed <<<<<\n\nx ======== x")
except Exception as e:
    logger.exception(e)
    raise e

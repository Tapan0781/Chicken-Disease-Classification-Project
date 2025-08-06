from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingetion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline


STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    data_ingestion_pipeline = DataIngestionTrainingPipeline()
    data_ingestion_pipeline.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Prepare Base Model Stage"
try:
        logger.info(f"**************")
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
        obj = PrepareBaseModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<")

except Exception as e:
        logger.exception(e)
        raise e 
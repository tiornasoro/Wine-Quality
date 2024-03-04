from Wine_Quality import logger
from Wine_Quality.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from Wine_Quality.pipeline.stage_02_data_validation import DataValidationTrainigPipeline

STAGE_NAME= "Data Ingestion stage"
try:
    logger.info(f" >>>>> stage {STAGE_NAME} started  <<<<<<<<<")
    data_ingestion=DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<\n\nx=========x")

except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME= "Data Validation stage"
try:
    logger.info(f" >>>>> stage {STAGE_NAME} started  <<<<<<<<<")
    data_ingestion=DataValidationTrainigPipeline()
    data_ingestion.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<\n\nx=========x")

except Exception as e:
    logger.exception(e)
    raise e

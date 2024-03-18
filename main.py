from Wine_Quality import logger
from Wine_Quality.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from Wine_Quality.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from Wine_Quality.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from Wine_Quality.pipeline.stage_04_model_trainer import ModelTrainerPipeline
from Wine_Quality.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline

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
    data_ingestion=DataValidationTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<\n\nx=========x")

except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME="Data Transformation stage"
try:
        logger.info(f" >>>>> stage {STAGE_NAME} started  <<<<<<<<<")
        obj=DataTransformationTrainingPipeline()
        obj.main()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<\n\nx=========x")

except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME="Model Trainer  stage"
try:
        logger.info(f" >>>>> stage {STAGE_NAME} started  <<<<<<<<<")
        obj=ModelTrainerPipeline()
        obj.main()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<\n\nx=========x")

except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME= "Model evaluation stage"
try:
    logger.info(f" >>>>> stage {STAGE_NAME} started  <<<<<<<<<")
    obj=ModelEvaluationTrainingPipeline()
    obj.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<\n\nx=========x")

except Exception as e:
    logger.exception(e)
    raise e
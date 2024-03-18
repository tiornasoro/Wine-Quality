from Wine_Quality.config.configuration import ConfigurationManager
from Wine_Quality.components.data_ingestion import DataIngestion
from Wine_Quality import logger
from pathlib import Path

STAGE_NAME= "Data Transformation stage"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            with open(Path("artifacts/data_validation/status.txt"),"r") as f:
                status=f.read().split(" ")[-1]

                if status=="True":
                    config=ConfigurationManager()
                    data_transformation_config= config.get_data_transformation_config()
                    data_transformation= data_transformation(config=data_transformation_config)
                    data_transformation.train_test_spliting()

                else:
                    raise Exception("Data Schema not valid")

        except Exception as e:
            print(e)

if __name__=='__main__':
    try:
        logger.info(f" >>>>> stage {STAGE_NAME} started  <<<<<<<<<")
        obj=DataTransformationTrainingPipeline()
        obj.main()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<\n\nx=========x")

    except Exception as e:
        logger.exception(e)
        raise e
        

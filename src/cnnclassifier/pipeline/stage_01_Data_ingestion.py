from cnnclassifier.components.Data_ingestion import DataIngestion
from cnnclassifier.config.configuration import ConfigurationManager
from cnnclassifier.entity.config_entity import DataIngestionConfig

from cnnclassifier import logger



STAGE_NAME = "Data Ingestion stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        Data_ingestion_config = config.get_Data_ingestion_config()
        data_ingestion = DataIngestion(config=Data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()




if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e

from housing.entity.config_entity import DataIngestionConfig,DataTransformationConfig,DataValidationConfig \
    ,ModelEvaluationConfig,ModelPusherConfig,ModelTrainerConfig,TrainingPipelineConfig
from housing.util.util import read_yaml_file
from housing.exception import HousingException
import os,sys
from housing.logger import logging

## we are going to import all the attributes from constant file
from housing.constant import *


class Configuration:

    def __init__(self,  
        config_file_path = CONFIG_FILE_PATH,
        current_time_stamp = CURRENT_TIME_STAMP
        ) -> None:

        self.config_info = read_yaml_file(file_path=config_file_path)
        self.config_training_pipeline = self.get_training_pipeline_config()
        self.time_stamp = current_time_stamp

        

    ## All of the functions will return entities.
    ## these functions will take in the namedtuple attributes which are the 
    ## entitities and will get the value which will be returned.

    ## from utility functions, read yaml function is used.


    def get_data_ingestion_config(self)->DataIngestionConfig:
        try:
            pass
        except Exception as e:
            raise HousingException(e,sys)

    def get_data_validation_config(self)->DataValidationConfig:
        try:
            pass
        except Exception as e:
            raise HousingException(e,sys)

    def get_data_transformation_config(self)->DataTransformationConfig:
        try:
            pass
        except Exception as e:
            raise HousingException(e,sys)

    def get_model_trainer_config(self)->ModelTrainerConfig:
        try:
            pass
        except Exception as e:
            raise HousingException(e,sys)

    def get_model_evaluation_config(self)->ModelEvaluationConfig:
        try:
            pass
        except Exception as e:
            raise HousingException(e,sys)
    
    def get_model_pusher_config(self)->ModelPusherConfig:
        try:
            pass
        except Exception as e:
            raise HousingException(e,sys)

    def get_training_pipeline_config(self)->TrainingPipelineConfig:
        try:
            training_pipeline_config = self.config_info[TRAINING_PIPELINE_CONFIG_KEY]
            ## here ,self.config_info is a dictionary read from yaml file
            ##       TRAINIG_PIPELINE_CONFIG_KEY is a key in the dictionary defined in our constant class.
            ##     and training_pipeline_config is a variable where we are storing its value.

            artifact_dir = os.path.join(ROOT_DIR,
            training_pipeline_config[TRAINING_PIPELINE_NAME_KEY],
            training_pipeline_config[TRAINING_PIPELINE_ARTIFACT_DIR_KEY])
            logging.info(f"Training_pipeline_config : {training_pipeline_config}")
            return training_pipeline_config


        except Exception as e:
            raise HousingException(e,sys) from e
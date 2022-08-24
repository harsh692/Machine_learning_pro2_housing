import os
from datetime import datetime

ROOT_DIR = os.getcwd() ## getting current working directory  

CONFIG_DIR = "config"

CONFIG_FILENAME = "config.yaml"

CONFIG_FILE_PATH = os.path.join(ROOT_DIR,CONFIG_DIR,CONFIG_FILENAME)

CURRENT_TIME_STAMP = f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"

## Training config pipeline variables  

TRAINING_PIPELINE_CONFIG_KEY = "training_pipeline_config" 
TRAINING_PIPELINE_ARTIFACT_DIR_KEY = "artifact_dir"
TRAINING_PIPELINE_NAME_KEY = "pipeline_name"

# the value of the above constants are the same as the keys defined in yaml file,
# therefore, we can get information from the file by using these keywords.
from fileinput import filename
import logging
from datetime import datetime
import os
from stat import filemode

LOG_DIR = "housing_logs"

CURRENT_TIMESTAMP = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}"

LOG_FILENEAME = f"log_{CURRENT_TIMESTAMP}.log" 

os.makedirs(LOG_DIR,exist_ok=True)  ## exist_ok checks if folder already exist or not
                                    ## it will only create the folder if not exist.

LOG_FILEPATH = os.path.join(LOG_DIR,LOG_FILENEAME)

logging.basicConfig(filename=LOG_FILEPATH,
    filemode="w",
    format='[%(asctime)s] %(name)s %(levelname)s - %(message)s',
    level=logging.INFO
    )
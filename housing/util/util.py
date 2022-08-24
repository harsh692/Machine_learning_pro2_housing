# util.py is a file containing all the utility functions which
# are to be used at any stage of the pipeling as a helper(small functionality).

import yaml
from housing.exception import HousingException
import os,sys

def read_yaml_file(file_path:str)->dict:
    """
    Description : Reads a yaml file and returns its contents in the form of dictionary.
    file_path : str
    """

    try: 
        with open(file_path,"rb") as f:
            return yaml.safe_load(f)

    except Exception as e:
        raise HousingException(e,sys) from e

    
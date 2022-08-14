from setuptools import setup
from typing import List

# DECLARING VARIABLES FOR SETUP FUNCTIONS

PROJECT_NAME = 'housing-predictor'
VERSION = '0.0.1'
AUTHOR_NAME = 'Harsh Gupta'
DESCRIPTION = 'This is the first full fledged ml project.'
PACKAGES = ['housing']
REQUIREMENT_FILE = 'requirements.txt'

def get_requirement_list()->List[str]: ## this will return a list with string value in it

    """
    DESCRIPTION : This function will read all the packages in the REQUIREMENT_FILE ,
    and return a list containing the packages mentioned in that file.

    RETURN : This function returns packages mentioned in the file which needs to be
    installed for the application to work in the form of a list of strings. 
    """

    with open(REQUIREMENT_FILE) as f:
        lis= f.readlines()
        return lis.remove('-e .') ## returning the list of mentioned packages in REQUIREMENT_FILE

setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR_NAME,
    description=DESCRIPTION,
    packages=PACKAGES,
    install_requires = get_requirement_list()
)


# Central file to manage all the methods and other files
# Code the files according to project goals and data then execute from here

import os
import sys
import pandas as pd
from src.exception import custom_exception
from src.logger import logging
from .data_ingesion import data_ingesion
from .data_transformation import data_transformation
from .model_trainer import model_trainer

if __name__ == '__main__':
    
    logging.info('Reading the data from source')
    try:
        df = pd.read_csv('artifacts/raw_dataset.csv')        # Add file name here
        logging.info('Data read successfully')
    except Exception as e:
        raise custom_exception(e, sys)
    
    logging.info('Data Ingesion started')
    ingesion_object = data_ingesion()
    transformed_data_path = ingesion_object.initiate_data_ingestion(df)
    logging.info('Data Ingestion completed')
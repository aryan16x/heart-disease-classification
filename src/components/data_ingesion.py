# Handle functions and objects of this file from project_manager

import os
import sys
from src.exception import custom_exception
from src.logger import logging
from dataclasses import dataclass
import pandas as pd
from sklearn.model_selection import train_test_split

# import other required libraries from here

@dataclass
class data_ingesion_config:
    train_data_path:str=os.path.join('artifacts','train.csv')
    test_data_path:str=os.path.join('artifacts','test.csv')
    raw_data_path:str=os.path.join('artifacts','data.csv')
    
class data_ingesion:
    def __init__(self):
        self.ingestion_config=data_ingesion_config()

    def initiate_data_ingestion(self,data_file_path):
        logging.info('Data Ingestion methods Starts')
        try:
            df = pd.read_csv(data_file_path)
            logging.info('Dataset read as pandas dataframe')
            
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)
            os.makedirs(os.path.dirname(self.ingestion_config.test_data_path), exist_ok=True)
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path), exist_ok=True)
            
            logging.info('Train test split initiated')
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
            logging.info('Train test split completed')
            
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
            logging.info('Artifacts have been saved')
            
            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,
                self.ingestion_config.raw_data_path
            )
        
        except Exception as e:
            raise custom_exception(e, sys)
                             
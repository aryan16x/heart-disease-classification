# Handle functions and objects of this file from project_manager

import os
import sys
from src.exception import custom_exception
from src.logger import logging
from dataclasses import dataclass
import pandas as pd
from .data_transformation import data_transformation
from .model_trainer import model_trainer
from sklearn.model_selection import train_test_split

@dataclass
class data_ingesion_config:
    transformed_data_path:str=os.path.join('artifacts','transformed_data.csv')
    
class data_ingesion:
    def __init__(self):
        self.ingestion_config=data_ingesion_config()

    def initiate_data_ingestion(self,dataframe_file):
        logging.info('Data Ingestion methods Starts')
        try:
            df = dataframe_file
            
            os.makedirs(os.path.dirname(self.ingestion_config.transformed_data_path), exist_ok=True)
            
            objx = data_transformation()
            df = objx.remove_nulls(df)
            
            df = objx.encode_labels(df)
            
            df.drop(df.columns[0], axis=1, inplace=True)
            
            logging.info('Train test split initiated')
            X_train, X_test, y_train, y_test = train_test_split(df.iloc[:,:-1], df.iloc[:,-1], test_size=0.2, random_state=42)
            logging.info('Train test split completed')
            
            modelx = model_trainer()
            modelx.initiate_model_trainer(X_train, X_test, y_train, y_test)
            
            df.to_csv(self.ingestion_config.transformed_data_path, index=False, header=True)
            logging.info('Artifacts have been saved')
            
            return(
                self.ingestion_config.transformed_data_path
            )
        
        except Exception as e:
            raise custom_exception(e, sys)
                             
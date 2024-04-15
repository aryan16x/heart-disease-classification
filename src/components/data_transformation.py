# Handle functions and objects of this file from project_manager

import os
import sys
import pandas as pd
import numpy as np
from src.exception import custom_exception
from src.logger import logging
# from src.utils import save_object
from dataclasses import dataclass
from sklearn.preprocessing import LabelEncoder
# from sklearn.pipeline import Pipeline
# from sklearn.compose import ColumnTransformer
# from sklearn.impute import SimpleImputer

@dataclass
class data_transform_config:
    train_data_path: str=os.path.join('artifacts','train.csv')
    test_data_path: str=os.path.join('artifacts','test.csv')
    preprocessor_ob_file_path: str = os.path.join('artifacts','preprocessor.pkl')

class data_transformation:
    def __init__(self):
        self.transform_config = data_transform_config()
        
    def get_transformation_object(self):
        try:
            logging.info("Preparing for preprcoessor")
            
            # Add the pipeline and Columntransformers here
            
            logging.info("Columntransformation object is created")
            return preprocessor

        except Exception as e:
            raise CustomException(e,sys)
    
    def remove_nulls(self,data):
        data.dropna(inplace=True)
        data.drop_duplicates(inplace=True)
        
        return data
    
    def encode_labels(self,df):
        label_encoder = LabelEncoder()
        df['sex'] = label_encoder.fit_transform(df['sex'])
        df['target'] = label_encoder.fit_transform(df['target'])
        
        return df
        
        
    def initiate_data_transoformer(self):
        try:
            try:
                logging.info("Reading train data")
                train_data = pd.read_csv("artifacts/train_data.csv")
                logging.info("Reading test data")
                test_data = pd.read_csv("artifacts/test_data.csv")
            except Exception as e:
                raise CustomException(e,sys)
    
            logging.info("Data Files have been fetched successfully in data transformer")
            
            preprocessing_obj = self.get_transformation_object()
            
            logging.info("Preprocessing object is created")
            
            # Add the code to tranform the data using preprocessing object
            
            logging.info("Data has been transformed successfully")
            return(
                train_arr,
                test_arr,
                self.transform_config.preprocessor_ob_file_path
            )
            
        except Exception as e:
            CustomException(e,sys)
            
if __name__ == '__main__':
    obj = data_transformation()
    train_arr, test_arr, path = obj.initiate_data_transoformer()
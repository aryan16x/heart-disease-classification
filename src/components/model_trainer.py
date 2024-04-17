import os
import sys
from dataclasses import dataclass
from src.exception import custom_exception
from src.logger import logging
from joblib import dump
import numpy as np

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


@dataclass
class model_trainer:
    def initiate_model_trainer(self,X_train, X_test, y_train, y_test):
        try:
            logging.info("Splitting features and target values")
        
            model = RandomForestClassifier()
            model.fit(np.array(X_train), np.array(y_train))
            predictions = model.predict(X_test)
            accuracy = accuracy_score(y_test, predictions)
            print("Accuracy:", accuracy)
            
            dump(model, 'artifacts/random_forest_model.joblib')
            
        except Exception as e:
            raise CustomException(e,sys)
import os
import sys
from dataclasses import dataclass
from src.exception import custom_exception
from src.logger import logging
# from src.utils import save_object,evaluate_models

# from catboost import CatBoostRegressor
# from sklearn.ensemble  import (
#     AdaBoostRegressor,
#     GradientBoostingRegressor,
#     RandomForestRegressor
# )
# from sklearn.linear_model import LinearRegression,Lasso,Ridge
# from sklearn.metrics import r2_score
# from sklearn.neighbors import KNeighborsRegressor
# from sklearn.tree import DecisionTreeRegressor
# from xgboost import XGBRegressor

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


@dataclass
class model_trainer:
    def initiate_model_trainer(self,X_train, X_test, y_train, y_test):
        try:
            logging.info("Splitting features and target values")
        
            model = RandomForestClassifier()
            model.fit(X_train, y_train)
            predictions = model.predict(X_test)
            accuracy = accuracy_score(y_test, predictions)
            print("Accuracy:", accuracy)
            
           # Add code to train, evaluate, compare and to select the best model
           # Save the best model
            
        except Exception as e:
            raise CustomException(e,sys)
# Prediction Pipeline

import os
import sys
from joblib import load
import pandas as pd
from src.exception import custom_exception
from src.logger import logging

if __name__ == '__main__':
    
    try:
    
        logging.info("Getting the data from the user")
        
        age = input("Enter the age: ")
        sex = input("Enter the sex {1 for male | 0 for female}: ")
        cp = input("Enter the chest pain type {1 for typical angina | 2 for atypical angina | 3 for non-anginal pain | 4 for asymptomatic}: ")
        trestbps = input("Enter the resting blood pressure: ")
        chol = input("Enter the cholestrol level: ")
        fbs = input("Enter the fasting blood sugar level {1 for true | 0 for false}: ")
        restecg = input("Enter the resting electrocardiographic results {0 for normal | 1 for having ST-T wave abnormality | 2 for showing probable or definite left ventricular hypertrophy by Estes' criteria}: ")
        thalach = input("Enter the maximum heart rate achieved: ")
        exang = input("Enter the exercise induced angina {1 for true | 0 for false}: ")
        oldpeak = input("Enter the ST depression induced by exercise relative to rest: ")
        slope = input("Enter the slope of the peak exercise ST segment {0 for upsloping | 1 for flat | 2 for downsloping}: ")
        ca = input("Enter the number of major vessels (0-3) colored by flourosopy: ")
        thal = input("Enter the thal: {1 for normal | 2 for fixed defect | 3 for reversable defect}: ")

        inputx = [[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]]
        # inputx = [[163, 1, 3, 145, 233, 1, 0, 150, 0, 2.3, 0, 0, 1]]
        # inputx = [[67, 0, 0 , 90, 200, 0, 0, 105, 0, 0, 0, 0, 3]]
        df = pd.DataFrame(inputx)
        
        model = load('artifacts/random_forest_model.joblib')
        
        class_probs = model.predict_proba(df)
        predicted_class_probs = class_probs.max(axis=1)
        
        print("Probability of Heart Disease: ", predicted_class_probs)
            
        
        
    except Exception as e:
        raise custom_exception(e,sys)
import os
import sys

# 1. Get the absolute path to the 'api' folder
API_DIR = os.path.dirname(os.path.abspath(__file__))

# 2. Add 'api' directly to Python's deployment search paths to help the joblib find the src folder
if API_DIR not in sys.path:
    sys.path.insert(0, API_DIR)

import joblib
import numpy as np
import pandas as pd
import sklearn


def predicting_price(property: dict):
    """
    Function loads a regression model and predict a price based on a property variables
    :param: a dictionary of the property variables
    Returns a float of the price
    """
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    MODEL_PATH = os.path.join(BASE_DIR, "..", "data", "pipeline_xgboost.pkl")

    pipeline = joblib.load(MODEL_PATH)
    expected_features_order = [
        'property_type', 'province', 'latitude', 'longitude', 'property_state',
        'build_year', 'bedroom_count', 'livable_surface', 'total_surface',
        'garage', 'terrace', 'energy_consumption_kWh/m2/year', 'swimming_pool',
        'preschool_distance_m', 'train_station_distance_m', 'supermarket_distance_m',
        'nearest_city_distance_km', 'Salary med/decla'
    ]

    df = pd.DataFrame([property])
    df = df[expected_features_order]
    y = np.expm1(pipeline.predict(df))[0]

    return y

if __name__ == '__main__':
    exemple = {
            'property_type': 'house',
            'province': 'antwerp',
            'latitude': np.nan,
            'longitude': np.nan,
            'property_state': 'New',
            'build_year': 2000.0,
            'bedroom_count': 5.0,
            'livable_surface': 200.0,
            'total_surface': 230.0,
            'garage': 1,
            'terrace': 0.0,
            'energy_consumption_kWh/m2/year': 188.0,
            'swimming_pool': 1,
            'preschool_distance_m': 600.0,
            'train_station_distance_m': 1000.0,
            'supermarket_distance_m': 350.0,
            'nearest_city_distance_km': 0.5,
            'Salary med/decla': 33000.0
        }
    y = predicting_price(exemple)
    print(y)
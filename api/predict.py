import joblib
import pandas as pd
import numpy as np
import sklearn


def predicting_price(property: dict):
    pipeline = joblib.load("../data/pipeline_xgboost.pkl")
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
"""
Data columns (total 19 columns):
 #   Column                          Non-Null Count  Dtype  
---  ------                          --------------  -----  
 0   property_type                   15744 non-null  str    
 1   province                        15744 non-null  str    
 2   latitude                        15744 non-null  float64
 3   longitude                       15744 non-null  float64
 4   price                           15744 non-null  int64  
 5   property_state                  15744 non-null  str    
 6   build_year                      9701 non-null   float64
 7   bedroom_count                   15366 non-null  float64
 8   livable_surface                 14828 non-null  float64
 9   total_surface                   14156 non-null  float64
 10  garage                          15744 non-null  int64  
 11  terrace                         15744 non-null  float64
 12  energy_consumption_kWh/m2/year  12839 non-null  float64
 13  swimming_pool                   15744 non-null  int64  
 14  preschool_distance_m            15678 non-null  float64
 15  train_station_distance_m        14868 non-null  float64
 16  supermarket_distance_m          15679 non-null  float64
 17  nearest_city_distance_km        15744 non-null  float64
 18  Salary med/decla                9662 non-null   float64
dtypes: float64(13), int64(3), str(3)
memory usage: 2.4 MB
PROVINCES : 
[       'antwerp',        'limburg',  'east-flanders', 'vlaams-brabant',
  'west-flanders',       'brussels',        'hainaut',          'liege',
     'luxembourg',          'namur', 'brabant-wallon']

Property_states : 
[           'Unknown',             'Normal',        'To renovate',
          'Excellent',                'New',    'Fully renovated',
        'To demolish', 'Under construction',         'To restore']

['apartment', 'house']
"""

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
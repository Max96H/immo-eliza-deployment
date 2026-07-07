import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin

class CustomFeatureEngineering(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self
        
    def transform(self, X):
        X = X.copy()
        X['is_in_nearest_city'] = (X['nearest_city_distance_km'] <= 5).astype(int)
        X['livable_surface_ratio'] = X['livable_surface'] / X['total_surface']
        X['average_room_size'] = X['livable_surface'] / X['bedroom_count'].replace(0, np.nan)
        X['near_train_station'] = (X['train_station_distance_m'] <= 1000).astype(int)
        X['isolation_score'] = X['preschool_distance_m'] + X['train_station_distance_m'] + X['supermarket_distance_m']
        X['new_building'] = (X['build_year'] >= 2020).astype(int)
        X['amenities'] = X['swimming_pool'] + X['garage'] + X['terrace']
        return X
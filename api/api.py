from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .predict import predicting_price
import numpy as np
import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
COORD_PATH = os.path.join(BASE_DIR, "..", "data", "zipcode_coordinates.csv")
SALARY_PATH = os.path.join(BASE_DIR, "..", "data", "salary_postcode.csv")

coordinates = pd.read_csv(COORD_PATH)
salaries = pd.read_csv(SALARY_PATH, sep=";")
salaries['Salary med/decla'] = salaries['Salary med/decla'].str.replace('\u202f', '', regex=False).astype(float)
coordinates['postcode'] = coordinates['postcode'].astype(str)
salaries['postcode'] = salaries['postcode'].astype(str)

app = FastAPI()

# Helps validate and parse query parameters
class Item(BaseModel):
    postcode: str
    property_type: str
    province: str
    property_state: str | None = 'Unknown'
    bedroom_count: int | None = None
    livable_surface: int | None = None
    total_surface: int | None = None
    energy_consumption_kWh: int | None = None
    terrace: bool | None = 0
    swimming_pool: bool | None = 0
    garage: bool | None = 0
    preschool_distance_m: int | None = None
    train_station_distance_m: int | None = None
    supermarket_distance_m: int | None = None
    nearest_city_distance_km: float | None = None
    build_year: int | None = None

@app.get("/")
def root():
    return "alive"

@app.post("/predict")
def predict(item: Item):
    """
    Function receives data, parses it, calls on a saved regression model and sends back the predicted price
    :param: a BaseModel of the query parameters
    Returns a dictionary with the price
    """
    property = item.model_dump()

    postcode = property.pop("postcode")

    if postcode not in coordinates["postcode"].values:
        raise HTTPException(status_code=400, detail="Invalid zipcode")
    
    property["latitude"], property["longitude"] = coordinates.loc[coordinates['postcode'] == postcode, ['latitude', 'longitude']].values[0]

    if postcode in salaries["postcode"].values:
        property["Salary med/decla"] = salaries.loc[salaries['postcode'] == postcode, 'Salary med/decla'].values[0]
    else:
        property["Salary med/decla"] = np.nan

    to_float = ['bedroom_count', "livable_surface", "total_surface", 
                "energy_consumption_kWh", "terrace", "preschool_distance_m",
                "train_station_distance_m", "supermarket_distance_m", 
                "build_year", "latitude", "longitude"]
    for col in to_float:
        property[col] = float(property[col])

    property["energy_consumption_kWh/m2/year"] = property.pop("energy_consumption_kWh")

    y = predicting_price(property)
    return {"prediction": round(float(y),2)}
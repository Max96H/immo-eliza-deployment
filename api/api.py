from fastapi import FastAPI
from pydantic import BaseModel
from .predict import predicting_price

app = FastAPI()

class Item(BaseModel):
    latitude: float
    longitude: float
    property_type: str
    province: str
    property_state: str | None = 'Unknown'
    bedroom_count: int | None = None
    livable_surface: float | None = None
    total_surface: float | None = None
    energy_consumption_kWh: float | None = None
    terrace: bool | None = 0
    swimming_pool: bool | None = 0
    garage: bool | None = 0
    preschool_distance_m: float | None = None
    train_station_distance_m: float | None = None
    supermarket_distance_m: float | None = None
    nearest_city_distance_km: float | None = None
    build_year: int | None = None

@app.get("/")
def root():
    return "alive"

@app.post("/predict")
def predict(item: Item):
    #print(item)
    print(type(item))
    property = item.model_dump()
    property["terrace"] = float(property["terrace"])
    property["build_year"] = float(property["build_year"])
    property["bedroom_count"] = float(property["bedroom_count"])
    property["energy_consumption_kWh/m2/year"] = property["energy_consumption_kWh"]
    del property["energy_consumption_kWh"]


    property["Salary med/decla"] = 33000.0

    y = predicting_price(property)
    return {"prediction": round(float(y),2)}
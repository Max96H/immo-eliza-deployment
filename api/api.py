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
    #print(item)
    print(type(item))
    property = item.model_dump()
    to_float = ['bedroom_count', "livable_surface", "total_surface", 
                "energy_consumption_kWh", "terrace", "preschool_distance_m",
                "train_station_distance_m", "supermarket_distance_m", 
                "build_year"]
    for col in to_float:
        property[col] = float(property[col])

    property["energy_consumption_kWh/m2/year"] = property["energy_consumption_kWh"]
    del property["energy_consumption_kWh"]

    # temporary mesure
    property["Salary med/decla"] = 33000.0

    y = predicting_price(property)
    return {"prediction": round(float(y),2)}
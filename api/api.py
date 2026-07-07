from fastapi import FastAPI
from pydantic import BaseModel
from predict import predict

app = FastAPI()

class Item(BaseModel):
    latitude: float
    longitude: float
    property_type: str
    province: str
    property_state: str | None = 'Unknown'
    livable_surface: int | None = None
    total_surface: int | None = None
    energy_consumption_kWh: int | None = None
    terrace: bool | None = 0
    swimming_pool: bool | None = 0
    garage: bool | None = 0
    preschool_distance_m: int | None = None
    train_station_distance_m: int | None = None
    supermarket_distance_m: int | None = None
    nearest_city_distance_km: int | None = None

@app.get("/")
async def root():
    return "alive"

@app.post("/predict")
async def predict(item: Item):
    property = {}

    y = predict(property)
    return {"prediction": y}
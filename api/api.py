from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    latitude: int
    longitude: int
    property_type: str
    livable_surface: int | None = None
    terrace: bool | None = 0
    swimming_pool: bool | None = 0
    garage: bool | None = 0
    swimming_pool: bool | None = 0
    swimming_pool: bool | None = 0


@app.get("/")
async def root():
    return "alive"

@app.post("/predict")
async def predict(item: Item):
    return {"prediction": 0}
from fastapi import FastAPI
from pydantic import BaseModel
import math

app = FastAPI()

# Request model
class Location(BaseModel):
    latitude: float
    longitude: float

# Example: fixed shop location (college / hostel / office)
SHOP_LAT = 20.2961   # Example Bhubaneswar latitude
SHOP_LON = 85.8245   # Example longitude

# Distance calculation
def distance_km(lat1, lon1, lat2, lon2):
    return math.sqrt((lat1-lat2)**2 + (lon1-lon2)**2) * 111

@app.post("/check-location")
def check_location(loc: Location):
    dist = distance_km(loc.latitude, loc.longitude, SHOP_LAT, SHOP_LON)

    if dist < 1:
        return {"status": "You are near the shop", "distance_km": round(dist,2)}
    else:
        return {"status": "Too far from shop", "distance_km": round(dist,2)}

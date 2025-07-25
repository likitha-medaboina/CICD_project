from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import joblib
import os

app = FastAPI()
model_path = os.path.join(os.path.dirname(__file__), 'model.pkl')
model = joblib.load(model_path)

class InputData(BaseModel):
    features: List[float]
    
@app.post("/predict")
def predict(data: InputData):
    prediction = model.predict([data.features])
    return {"prediction": int(prediction[0])}

from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel
import pickle, os
import numpy as np

app = FastAPI()

# Add logging

class InputData(BaseModel):
    "__doctring__"
    distance: float

def load_model():
    "__doctring__"
    model_path = os.path.join("..", "assets", "ml_components", "RegressionLinear_model.sav") 
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
    return model

# Chargez le modèle une seule fois au démarrage du serveur
model = load_model()

# Endpoints 
@app.get("/")
def read_root():
    "__doctring__"
    return {"Hello": "World"}
    
@app.post("/predict")
def predict(input_data: InputData):
    "__doctring__"
    data = np.array([[input_data.distance]])  # Inclure les deux caractéristiques
    predictions = model.predict(data)
    time = predictions[0].tolist()

    return {"Time from Pickup to Arrival": time}

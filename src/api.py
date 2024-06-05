from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np

app = FastAPI()

class InputData(BaseModel):
    distance: float

@app.get("/")
def read_root():
    return {"Hello": "World"}

def load_model():
    model_path = "../assets/ml_components/RegressionLinear_model.sav"
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
    return model

# Chargez le modèle une seule fois au démarrage du serveur
model = load_model()

@app.post("/predict")
def predict(input_data: InputData):
    data = np.array([[input_data.distance]])  # Inclure les deux caractéristiques
    predictions = model.predict(data)
    time = predictions[0].tolist()

    return {"Time from Pickup to Arrival": time}

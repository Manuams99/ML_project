from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import sklearn
import numpy as np

app = FastAPI()


class InputData(BaseModel):
    stay_class: int  # 1, 2, 3
    sex: int  
    ticket_price: float

@app.get("/")
def read_root():
    return {"Hello": "World"}

def load_model():
    model_path = "../assets/mlcomponents/RandomForestClassifier_model.pkl"  
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
    return model

# Chargez le modèle 
model = load_model()

@app.post("/predict")
def predict(input_data: InputData):
    data = np.array([[input_data.stay_class, input_data.sex, input_data.ticket_price]])
    predictions = model.predict(data)
    survival = predictions[0]
    survival = int(survival)

    return {"Survival Prediction": survival}

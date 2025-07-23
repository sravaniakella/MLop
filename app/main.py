from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import joblib

app = FastAPI()

# Load model
model = joblib.load("score_train_model.pkl")

class StudentData(BaseModel):
    study_time: float
    attendance: float
    gender_Male: int

@app.get("/")
def root_data():
    return {"message": "Hi, I am Sravani"}

@app.post("/predict")
def scr_prd(data: StudentData):
    inp_data = np.array([[data.study_time, data.attendance, data.gender_Male]])
    prd = model.predict(inp_data)
    return {"Predicted_score": int(prd[0])}

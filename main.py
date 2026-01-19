import joblib
import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="Breast Cancer Prediction API",
    description="ML-powered breast cancer classification system",
    version="1.0.0"
)

# -----------------------
# Health check
# -----------------------
@app.get("/")
def health_check():
    return {"status": "API is running"}

# -----------------------
# Load model and scaler
# -----------------------
model = joblib.load("./model/model.pkl")
scaler = joblib.load("./model/scaler.pkl")

# -----------------------
# Input schema
# -----------------------
class TumorInput(BaseModel):
    radius_mean: float
    texture_mean: float
    perimeter_mean: float
    area_mean: float
    smoothness_mean: float
    compactness_mean: float
    concavity_mean: float
    concave_points_mean: float
    symmetry_mean: float
    fractal_dimension_mean: float
    radius_se: float
    texture_se: float
    perimeter_se: float
    area_se: float
    smoothness_se: float
    compactness_se: float
    concavity_se: float
    concave_points_se: float
    symmetry_se: float
    fractal_dimension_se: float
    radius_worst: float
    texture_worst: float
    perimeter_worst: float
    area_worst: float
    smoothness_worst: float
    compactness_worst: float
    concavity_worst: float
    concave_points_worst: float
    symmetry_worst: float
    fractal_dimension_worst: float

# -----------------------
# Prediction endpoint
# -----------------------
@app.post("/predict")
def predict(data: TumorInput):
    X = np.array([list(data.dict().values())])
    X_scaled = scaler.transform(X)

    pred = model.predict(X_scaled)[0]
    proba = model.predict_proba(X_scaled)[0]

    return {
        "prediction": "Malignant" if pred == 1 else "Benign",
        "confidence": float(np.max(proba))
    }

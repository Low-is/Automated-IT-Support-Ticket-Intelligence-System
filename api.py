from fastapi import FastAPI
import pandas as pd
import joblib

# Create API app
app = FastAPI()

# Load model
model = joblib.load("model/ticket_priority_model.pkl")
model_features = joblib.load("model/model_features.pkl")

@app.post("/predict") # Creating API endpoint 
def predict(ticket: dict):

    print(ticket)

    df = pd.DataFrame([ticket])
    df = pd.get_dummies(df)

    df = df.reindex(columns=model_features, fill_value=0)

    prob = float(model.predict_proba(df)[0][1])
    
    print(type(prob))
    flag = prob > 0.7

    return {
        "high_priority_probability": prob,
        "flag": flag
    }
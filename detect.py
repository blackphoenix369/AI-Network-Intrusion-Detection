import pandas as pd
import joblib

# Load model
model = joblib.load("nids_model.pkl")

# Load data
df = pd.read_csv("traffic_data.csv")

X = df.copy()

# Predict
df["prediction"] = model.predict(X)
df["prediction"] = df["prediction"].map({0: "Normal", 1: "Intrusion"})

print(df[["packet_size", "packet_rate", "prediction"]].head())

import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="AI-Based NIDS", layout="wide")

st.title("🛡️ AI-Based Network Intrusion Detection System")

# Load model & data
model = joblib.load("nids_model.pkl")
df = pd.read_csv("traffic_data.csv")

st.subheader("📄 Network Traffic Dataset")
st.dataframe(df.head())

if st.button("🔍 Run Intrusion Detection"):
    predictions = model.predict(df)
    df["Status"] = ["Intrusion" if p == 1 else "Normal" for p in predictions]

    st.subheader("🚦 Detection Results")
    st.dataframe(df[["packet_size", "packet_rate", "Status"]])

    intrusion_count = df["Status"].value_counts().get("Intrusion", 0)
    st.metric("🚨 Intrusions Detected", intrusion_count)

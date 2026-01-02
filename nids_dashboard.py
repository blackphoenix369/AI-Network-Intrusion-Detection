import streamlit as st
import pandas as pd
import time

st.set_page_config(layout="wide")
st.title("🛡️ AI-Based Network Intrusion Detection System")

refresh = st.sidebar.slider("Refresh Interval (seconds)", 1, 5, 2)

def color_rows(row):
    if row.final_alert == "ATTACK":
        return ["background-color:#ff4d4d"] * len(row)
    return [""] * len(row)

while True:
    try:
        df = pd.read_csv("traffic_data.csv")
        df = df.tail(200).iloc[::-1]

        st.subheader("📡 Live Packet View")
        st.dataframe(
            df.style.apply(color_rows, axis=1),
            height=500
        )

        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Total Packets", len(df))
        col2.metric("Attacks", len(df[df.final_alert == "ATTACK"]))
        col3.metric("TCP Packets", len(df[df.protocol == "TCP"]))
        col4.metric("Unique Sources", df.src_ip.nunique())

        if len(df[df.final_alert == "ATTACK"]) > 0:
            st.error("🚨 Intrusion Detected!")

    except Exception as e:
        st.warning("Waiting for traffic...")

    time.sleep(refresh)
    st.rerun()

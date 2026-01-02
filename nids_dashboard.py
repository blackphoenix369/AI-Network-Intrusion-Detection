import streamlit as st
import pandas as pd
import time

st.set_page_config(layout="wide")
st.title("🛡️ AI-Based Network Intrusion Detection System")

placeholder = st.empty()

while True:
    try:
        df = pd.read_csv("traffic_data.csv")
        df = df.tail(100).iloc[::-1]

        def highlight(row):
            return ["background-color: #ffcccc" if row.final_label == "ATTACK" else "" for _ in row]

        with placeholder.container():
            st.subheader("📡 Live Packet Monitoring")
            st.dataframe(df.style.apply(highlight, axis=1), height=500)

            c1, c2, c3 = st.columns(3)
            c1.metric("Total Packets", len(df))
            c2.metric("Attacks", len(df[df.final_label == "ATTACK"]))
            c3.metric("Unique Sources", df.src_ip.nunique())

    except:
        st.warning("Waiting for traffic...")

    time.sleep(2)
    st.rerun()

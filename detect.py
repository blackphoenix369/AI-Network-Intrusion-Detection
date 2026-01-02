import pandas as pd
import joblib

model = joblib.load("nids_model.pkl")

df = pd.read_csv("traffic_data.csv")

df["syn_flag"] = df["tcp_flags"].str.contains("SYN").astype(int)

# ML Prediction
df["ml_prediction"] = model.predict(df[["packet_len", "syn_flag"]])

# Rule-based detection
def apply_rules(row):
    if row["syn_flag"] == 1 and row["packet_len"] < 100:
        return "SYN_FLOOD"
    return "NORMAL"

df["rule_alert"] = df.apply(apply_rules, axis=1)

df["final_label"] = df.apply(
    lambda r: "ATTACK" if r["rule_alert"] != "NORMAL" or r["ml_prediction"] == 1 else "NORMAL",
    axis=1
)

df.to_csv("traffic_data.csv", index=False)
print("✅ Detection completed")

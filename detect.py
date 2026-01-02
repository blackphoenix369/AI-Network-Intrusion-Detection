import pandas as pd
import joblib

model = joblib.load("nids_model.pkl")

df = pd.read_csv("traffic_data.csv")

df["syn_flag"] = df["tcp_flags"].str.contains("SYN").astype(int)

# Flow aggregation
flows = df.groupby("src_ip").agg(
    syn_count=("syn_flag", "sum"),
    packet_count=("packet_len", "count"),
    avg_packet_size=("packet_len", "mean")
).reset_index()

# ML prediction
flows["ml_alert"] = model.predict(
    flows[["syn_count", "packet_count", "avg_packet_size"]]
)

# Rule engine
def rule_engine(row):
    if row.syn_count > 100:
        return "SYN_FLOOD"
    return "NORMAL"

flows["rule_alert"] = flows.apply(rule_engine, axis=1)

flows["final_alert"] = flows.apply(
    lambda r: "ATTACK" if r.rule_alert != "NORMAL" or r.ml_alert == 1 else "NORMAL",
    axis=1
)

# Merge back to packets
df = df.merge(
    flows[["src_ip", "final_alert"]],
    on="src_ip",
    how="left"
)

df.to_csv("traffic_data.csv", index=False)
print("✅ Hybrid detection completed")

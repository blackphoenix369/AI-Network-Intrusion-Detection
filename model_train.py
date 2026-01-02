import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

df = pd.read_csv("traffic_data.csv")

# Feature Engineering
df["syn_flag"] = df["tcp_flags"].str.contains("SYN").astype(int)

# Flow aggregation
flow_stats = df.groupby("src_ip").agg(
    syn_count=("syn_flag", "sum"),
    packet_count=("packet_len", "count"),
    avg_packet_size=("packet_len", "mean")
).reset_index()

# Label: SYN flood heuristic
flow_stats["label"] = (flow_stats["syn_count"] > 50).astype(int)

X = flow_stats[["syn_count", "packet_count", "avg_packet_size"]]
y = flow_stats["label"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier(
    n_estimators=200,
    max_depth=10,
    random_state=42
)
model.fit(X_train, y_train)

joblib.dump(model, "nids_model.pkl")
print("✅ Flow-based ML model trained & saved")

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

df = pd.read_csv("traffic_data.csv")

# Simple feature engineering
df["syn_flag"] = df["tcp_flags"].str.contains("SYN").astype(int)

X = df[["packet_len", "syn_flag"]]
y = (df["syn_flag"] == 1).astype(int)  # SYN flood proxy label

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

joblib.dump(model, "nids_model.pkl")
print("✅ Model trained & saved as nids_model.pkl")

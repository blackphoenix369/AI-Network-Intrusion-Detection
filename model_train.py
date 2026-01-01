import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

# Load traffic data
df = pd.read_csv("traffic_data.csv")

# Create labels (simulation logic)
# High packet rate = intrusion
df["label"] = (df["packet_rate"] > 60).astype(int)

X = df.drop("label", axis=1)
y = df["label"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)

# Save model
joblib.dump(model, "nids_model.pkl")

print("✅ Model trained successfully")
print(f"🎯 Accuracy: {accuracy:.2f}")

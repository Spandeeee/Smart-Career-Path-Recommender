import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import joblib
import os

# Make sure 'model' directory exists
os.makedirs("model", exist_ok=True)

# Load dataset
df = pd.read_csv("data/career_dataset.csv")

# Separate features and target
X = df.drop("Recommended_Career", axis=1)
y = df["Recommended_Career"]

# One-hot encode features
X = pd.get_dummies(X)

# Encode target
le = LabelEncoder()
y_encoded = le.fit_transform(y)

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save model and encoder
joblib.dump(model, "model/career_model.pkl")
joblib.dump(le, "model/label_encoder.pkl")

print("✅ Model and encoder saved successfully.")

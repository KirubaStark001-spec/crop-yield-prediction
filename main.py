import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
import joblib

# Load dataset
df = pd.read_csv("data set/datafile (1).csv")

# Remove extra spaces
df.columns = df.columns.str.strip()

# Encode text columns
crop_encoder = LabelEncoder()
state_encoder = LabelEncoder()

df["Crop"] = crop_encoder.fit_transform(df["Crop"])
df["State"] = state_encoder.fit_transform(df["State"])

# Features and Target
X = df.drop("Yield (Quintal/ Hectare)", axis=1)
y = df["Yield (Quintal/ Hectare)"]

# Train Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train Model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Accuracy
y_pred = model.predict(X_test)
score = r2_score(y_test, y_pred)

print("Accuracy Score:", score)

# Save model
joblib.dump(model, "model/crop_yield_model.pkl")
print("Model Saved Successfully")
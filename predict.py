import joblib

# Load saved model
model = joblib.load("model/crop_yield_model.pkl")

# Input values
crop = int(input("Enter Crop Code: "))
state = int(input("Enter State Code: "))
cost_a2fl = float(input("Enter Cost of Cultivation A2+FL: "))
cost_c2 = float(input("Enter Cost of Cultivation C2: "))
production_cost = float(input("Enter Cost of Production C2: "))

# Predict
prediction = model.predict(
    [[crop, state, cost_a2fl, cost_c2, production_cost]]
)

print("\nPredicted Yield:", prediction[0])
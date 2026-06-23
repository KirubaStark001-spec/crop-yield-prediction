import streamlit as st
import joblib
import pandas as pd

# Page Configuration
st.set_page_config(
    page_title="Crop Yield Prediction",
    page_icon="🌾",
    layout="centered"
)

# Load Model
model = joblib.load("Model/crop_yield_model.pkl")

# Title
st.title("🌾 Crop Yield Prediction System")
st.markdown("Predict crop yield using Machine Learning (Random Forest Model)")

st.divider()

# User Inputs
st.subheader("Enter Crop Details")

crop = st.number_input(
    "Crop Code",
    min_value=0,
    value=0,
    help="Enter encoded crop value"
)

state = st.number_input(
    "State Code",
    min_value=0,
    value=0,
    help="Enter encoded state value"
)

cost_a2fl = st.number_input(
    "Cost of Cultivation (A2+FL)",
    min_value=0.0,
    value=10000.0
)

cost_c2 = st.number_input(
    "Cost of Cultivation (C2)",
    min_value=0.0,
    value=20000.0
)

production_cost = st.number_input(
    "Cost of Production (C2)",
    min_value=0.0,
    value=1500.0
)

# Prediction Button
if st.button("Predict Yield", use_container_width=True):

    input_data = pd.DataFrame(
        [[crop, state, cost_a2fl, cost_c2, production_cost]],
        columns=[
            "Crop",
            "State",
            "Cost of Cultivation (`/Hectare) A2+FL",
            "Cost of Cultivation (`/Hectare) C2",
            "Cost of Production (`/Quintal) C2"
        ]
    )

    prediction = model.predict(input_data)

    st.success(f"Predicted Yield: {prediction[0]:.2f} Quintal/Hectare")

    st.balloons()

# Footer
st.divider()
st.caption("Developed using Python, Scikit-Learn and Streamlit")

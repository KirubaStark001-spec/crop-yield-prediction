import streamlit as st
import joblib
import pandas as pd

# Page Configuration
st.set_page_config(
    page_title="Crop Yield Prediction",
    page_icon="🌾",
    layout="wide"
)

# Title
st.title("🌾 Crop Yield Prediction System")
st.markdown("Predict crop yield using Machine Learning")

# Load Model
try:
    model = joblib.load("crop_yield_model.pkl")
    st.success("✅ Model Loaded Successfully")
except Exception as e:
    st.error(f"❌ Error Loading Model: {e}")
    st.stop()

# Sidebar
st.sidebar.header("Input Parameters")

# User Inputs
rainfall = st.sidebar.number_input(
    "Rainfall (mm)",
    min_value=0.0,
    max_value=5000.0,
    value=1000.0
)

temperature = st.sidebar.number_input(
    "Temperature (°C)",
    min_value=0.0,
    max_value=50.0,
    value=25.0
)

fertilizer = st.sidebar.number_input(
    "Fertilizer Used (kg)",
    min_value=0.0,
    max_value=1000.0,
    value=100.0
)

area = st.sidebar.number_input(
    "Area (hectares)",
    min_value=0.1,
    max_value=10000.0,
    value=10.0
)

# Create DataFrame
input_data = pd.DataFrame({
    "Rainfall": [rainfall],
    "Temperature": [temperature],
    "Fertilizer": [fertilizer],
    "Area": [area]
})

st.subheader("Input Data")
st.dataframe(input_data)

# Prediction
if st.button("🔍 Predict Yield"):

    try:
        prediction = model.predict(input_data)

        st.success("Prediction Completed")

        st.metric(
            label="🌾 Predicted Crop Yield",
            value=f"{prediction[0]:.2f}"
        )

    except Exception as e:
        st.error(f"Prediction Error: {e}")

# Footer
st.markdown("---")
st.markdown("Developed using Streamlit & Machine Learning")

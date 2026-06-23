import streamlit as st
import pandas as pd
import joblib

# Page Config
st.set_page_config(
    page_title="🌾 Crop Yield Prediction",
    page_icon="🌱",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
.stApp{
    background: linear-gradient(135deg,#d4fc79,#96e6a1);
}

.main-title{
    text-align:center;
    font-size:45px;
    font-weight:bold;
    color:#0b4f2c;
}

.glass{
    background: rgba(255,255,255,0.2);
    backdrop-filter: blur(10px);
    padding:20px;
    border-radius:20px;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="main-title">🌾 Smart Crop Yield Prediction</p>',
            unsafe_allow_html=True)

# Load Model
try:
    model = joblib.load("crop_yield_model.pkl")
except Exception as e:
    st.error(f"Model Loading Error: {e}")
    st.stop()

# Inputs
st.markdown('<div class="glass">', unsafe_allow_html=True)

crop = st.text_input("Crop Name")

state = st.text_input("State Name")

cost_a2fl = st.number_input(
    "Cost of Cultivation (₹/Hectare) A2+FL",
    min_value=0.0
)

cost_c2 = st.number_input(
    "Cost of Cultivation (₹/Hectare) C2",
    min_value=0.0
)

production_c2 = st.number_input(
    "Cost of Production (₹/Quintal) C2",
    min_value=0.0
)

st.markdown('</div>', unsafe_allow_html=True)

if st.button("🌱 Predict Yield"):

    input_df = pd.DataFrame({
        "Crop":[crop],
        "State":[state],
        "Cost of Cultivation (`/Hectare) A2+FL":[cost_a2fl],
        "Cost of Cultivation (`/Hectare) C2":[cost_c2],
        "Cost of Production (`/Quintal) C2":[production_c2]
    })

    try:
        prediction = model.predict(input_df)

        st.success("Prediction Completed Successfully")

        st.metric(
            label="🌾 Predicted Yield",
            value=f"{prediction[0]:.2f}"
        )

    except Exception as e:
        st.error(f"Prediction Error: {e}")

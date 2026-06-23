import streamlit as st
import sys
import os

st.set_page_config(
    page_title="Crop Yield Prediction",
    page_icon="🌾",
    layout="wide"
)

st.title("🌾 Crop Yield Prediction")
st.write("## Debug Information")

st.write("### Python Version")
st.code(sys.version)

st.write("### Current Directory")
st.code(os.getcwd())

st.write("### Files in Repository")
st.write(os.listdir())

try:
    import joblib
    st.success("✅ Joblib Installed Successfully")
except Exception as e:
    st.error(f"❌ Joblib Error: {e}")

try:
    import sklearn
    st.success("✅ Scikit-Learn Installed Successfully")
except Exception as e:
    st.error(f"❌ Scikit-Learn Error: {e}")

try:
    import pandas
    st.success("✅ Pandas Installed Successfully")
except Exception as e:
    st.error(f"❌ Pandas Error: {e}")

try:
    import numpy
    st.success("✅ NumPy Installed Successfully")
except Exception as e:
    st.error(f"❌ NumPy Error: {e}")

st.write("### End of Debug")

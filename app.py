import streamlit as st
import joblib
import numpy as np

# Load model and scaler
model = joblib.load('logistic_model.pkl')
scaler = joblib.load('scaler.pkl')

st.title("Credit Card Fraud Detection")

st.markdown("### Enter transaction details:")

# Actual feature names (30 total: Time, V1–V28, Amount)
feature_names = ['Time'] + [f'V{i}' for i in range(1, 29)] + ['Amount']

# Create input fields
inputs = []
for name in feature_names:
    value = st.number_input(name, value=0.0)
    inputs.append(value)

# Predict button
if st.button("Check for Fraud"):
    inputs_scaled = scaler.transform([inputs])
    prediction = model.predict(inputs_scaled)

    if prediction[0] == 1:
        st.error("⚠️ Fraudulent Transaction Detected!")
    else:
        st.success("Legitimate Transaction")

import streamlit as st
import joblib
import numpy as np

# Load model and scaler
model = joblib.load('logistic_model.pkl')
scaler = joblib.load('scaler.pkl')

st.title("Credit Card Fraud Detection")

# Intro and instructions
st.markdown("""
🔍 **Detect Fraud in Real-Time!**  
Enter transaction details manually or use a known fraud example to test the model.  
Click **"Check for Fraud"** to get results.

⚠️ For demo purposes only.
""")

st.markdown("### Enter transaction details:")

# Actual feature names (30 total: Time, V1–V28, Amount)
feature_names = ['Time'] + [f'V{i}' for i in range(1, 29)] + ['Amount']

# Example fraudulent transaction
fraud_example = [
    406.0, -2.3122265423263, 1.9519920106416, -1.60985073229769,
    3.9979055875468, -0.522187864667398, -1.42654531920595, -2.53738730624559,
    1.39165724832302, -2.77008927771812, -2.77227214493964, 3.20203320709635,
    -2.89990738849473, -0.595221881324605, -4.28925378244248, 0.389724820543719,
    -1.14074717980657, -2.830055674504, -0.0100160633496401, 0.277837575558899,
    -1.51465432260541, 0.207642865265889, 0.624501459424895, 0.0660836852680535,
    0.717292731410831, -0.165945922526734, 2.3458649490158, -1.89033174624551,
    -0.638067933317427, 0.0
]

# Initialize session state
if 'inputs' not in st.session_state:
    st.session_state.inputs = [0.0] * 30

# Button to autofill fraud example
if st.button("🔍 Use Example Fraud Data"):
    st.session_state.inputs = fraud_example

# Input fields
inputs = []
for i, name in enumerate(feature_names):
    value = st.number_input(name, value=st.session_state.inputs[i], key=name)
    inputs.append(value)

# Prediction
if st.button("Check for Fraud"):
    try:
        inputs_scaled = scaler.transform([inputs])
        prediction = model.predict(inputs_scaled)

        if prediction[0] == 1:
            st.error("⚠️ Fraudulent Transaction Detected!")
        else:
            st.success("Legitimate Transaction")
    except Exception as e:
        st.error(f"An error occurred: {e}")

import streamlit as st
import requests

# Title and Instructions
st.title("🎓 Student Pass/Fail Predictor")
st.write("Enter marks for 3 subjects to predict whether the student will pass or fail.")

# Input Fields
mark1 = st.number_input("Subject 1 Marks", min_value=0, max_value=100)
mark2 = st.number_input("Subject 2 Marks", min_value=0, max_value=100)
mark3 = st.number_input("Subject 3 Marks", min_value=0, max_value=100)

# Combine inputs into a feature list
features = [mark1, mark2, mark3]

# Predict Button
if st.button("Predict"):
    response = requests.post(
        "http://127.0.0.1:8000/predict",
        json={"features": features}
    )

    if response.status_code == 200:
        result = response.json()
        prediction = result.get("prediction")

        # Corrected output message
        st.write(f"The model prediction: {'✅ Pass' if prediction == 1 else '❌ Fail'}")
    else:
        st.error(f"Server error: {response.status_code}")

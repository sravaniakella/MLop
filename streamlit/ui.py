import streamlit as st
import requests

# Title
st.title("🎓✅ Score Predictor ✅")

# Input widgets
study_time = st.slider("📚 Study Time (in hours)", 0, 10)
attendance = st.slider("📅 Attended Days", 0, 80)
gender = st.selectbox("🧑‍🤝‍🧑 Gender", ["Male", "Female"])

# Gender encoding for the model
gender_val = 1 if gender == "Male" else 0

# Predict button
if st.button("Predict"):
    # Data payload
    data = {
        "study_time": study_time,
        "attendance": attendance,
        "gender_Male": gender_val
    }

    # API call to FastAPI backend
    try:
        response = requests.post("https://abc-stud-1.onrender.com/predict", json=data)
        
        if response.status_code == 200:
            result = response.json()
            st.success(f"🎯 Predicted Score: {result['Predicted_score']}")
        else:
            st.error(f"❌ API Error: {response.status_code} - {response.text}")
    
    except Exception as e:
        st.error(f"🔌 Couldn't connect to API. Error: {e}")

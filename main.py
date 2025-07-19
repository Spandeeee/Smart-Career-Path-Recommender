import streamlit as st
import pandas as pd
import joblib
from ui import user_input_form
from roadmap_generator import get_roadmap

# Load model and encoder
model = joblib.load("model/career_model.pkl")
le = joblib.load("model/label_encoder.pkl")

st.set_page_config(page_title="Smart Career Recommender", layout="centered")

st.title("🔮 Smart Career Path Recommender")

user_input = user_input_form()

if st.button("Get Career Recommendation"):
    df = pd.DataFrame([user_input])
    df = pd.get_dummies(df)  # One-hot encode
    df = df.reindex(columns=model.feature_names_in_, fill_value=0)
    
    pred = model.predict(df)
    career = le.inverse_transform(pred)[0]
    
    st.success(f"🌟 Recommended Career: **{career}**")
    
    roadmap = get_roadmap(career)
    st.subheader("📌 Career Roadmap:")
    for step in roadmap:
        st.markdown(f"- {step}")

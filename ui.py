import streamlit as st

def user_input_form():
    st.header("🎓 Career Recommendation Form")
    subject_interest = st.selectbox("Interest in Subjects", ["High", "Medium", "Low"])
    coding = st.selectbox("Coding Skills", ["High", "Medium", "Low"])
    creativity = st.selectbox("Creativity", ["High", "Medium", "Low"])
    communication = st.selectbox("Communication Skills", ["High", "Medium", "Low"])
    subject = st.selectbox("Preferred Subject", ["Computer Science", "Biology", "Commerce", "Arts"])
    
    return {
        "Subject_Interest": subject_interest,
        "Coding_Skills": coding,
        "Creativity": creativity,
        "Communication": communication,
        "Preferred_Subject": subject
    }

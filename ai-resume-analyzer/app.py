import streamlit as st

keywords = ["python", "java", "sql", "react", "node"]

st.title("AI Resume Analyzer")

text = st.text_area("Paste resume text:")

if st.button("Analyze"):
    matched = [k for k in keywords if k in text.lower()]
    score = len(matched) / len(keywords) * 100
    st.write("Match Score:", score)
    st.write("Matched Keywords:", matched)

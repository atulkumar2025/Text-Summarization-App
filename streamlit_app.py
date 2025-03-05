import streamlit as st
from abstractive import abstractive_summary

st.title("Text Summarization App")
text = st.text_area("Enter text to summarize")

if st.button("Summarize"):
    summary = abstractive_summary(text)
    st.write("Summary:", summary)

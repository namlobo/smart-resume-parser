import streamlit as st
from parser import parse_resume
from pdf_reader import pdf_to_text

st.set_page_config(page_title="Smart Resume Parser", layout="centered")

st.title("📄 Smart Resume Parser using Hugging Face")

uploaded_file = st.file_uploader("Upload Resume PDF", type=["pdf"])

if uploaded_file:
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    text = pdf_to_text("temp.pdf")

    st.subheader("Extracted Resume Text")
    st.text_area("", text, height=200)

    result = parse_resume(text)

    st.subheader("📊 Parsed Resume Information")
    st.json(result)
st.markdown("""
<style>
body { background-color: #0e1117; color: white; }
</style>
""", unsafe_allow_html=True)

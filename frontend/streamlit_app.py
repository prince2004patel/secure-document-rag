import streamlit as st
import requests

BACKEND_URL = "http://127.0.0.1:5000"

st.set_page_config(
    page_title="Secure Document Query System",
    layout="wide"
)

st.title("Secure Document Query System")

st.write("RAG-Based Secure Document Question Answering")

st.divider()

# Backend Status

st.subheader("Backend Status")

if st.button("Check Backend"):

    try:
        response = requests.get(f"{BACKEND_URL}/health")

        if response.status_code == 200:
            st.success("Backend Connected Successfully ✅")
            st.json(response.json())

        else:
            st.error("Backend Error")

    except Exception as e:
        st.error("Cannot connect to Flask Backend")
        st.write(e)

st.divider()

# Upload Section

st.subheader("Upload Document")

uploaded_file = st.file_uploader(
    "Upload PDF or DOCX",
    type=["pdf", "docx"]
)

if uploaded_file:
    st.info(f"Selected File: {uploaded_file.name}")

    if st.button("Upload"):
        st.success("Upload functionality will be added in Phase 4.")

st.divider()

# Query Section

st.subheader("Ask Question")

question = st.text_input("Enter your question")

if st.button("Ask"):

    if question == "":
        st.warning("Please enter a question.")

    else:
        st.success("RAG functionality will be added in Phase 5.")
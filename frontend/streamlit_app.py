import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:5000"

st.set_page_config(
    page_title="Secure Document Query System",
    layout="wide"
)

# Session State

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "user_id" not in st.session_state:
    st.session_state.user_id = None

if "username" not in st.session_state:
    st.session_state.username = None

# Login / Register

if not st.session_state.logged_in:

    option = st.sidebar.selectbox(
        "Select",
        ["Login", "Register"]
    )

    if option == "Register":

        st.title("Create Account")

        username = st.text_input("Username")

        email = st.text_input("Email")

        password = st.text_input(
            "Password",
            type="password"
        )

        if st.button("Register"):

            response = requests.post(

                BASE_URL + "/register",

                json={

                    "username": username,

                    "email": email,

                    "password": password

                }

            )

            data = response.json()

            if response.status_code == 200:

                st.success(data["message"])

            else:

                st.error(data["error"])

    else:

        st.title("Login")

        email = st.text_input("Email")

        password = st.text_input(
            "Password",
            type="password"
        )

        if st.button("Login"):

            response = requests.post(

                BASE_URL + "/login",

                json={

                    "email": email,

                    "password": password

                }

            )

            data = response.json()

            if response.status_code == 200:

                st.session_state.logged_in = True
                st.session_state.user_id = data["user_id"]
                st.session_state.username = data["username"]

                st.rerun()

            else:

                st.error(data["error"])

# Dashboard

else:

    st.title("Secure Document Query System")

    st.success(
        f"Welcome {st.session_state.username}"
    )

    st.divider()

    st.subheader("Upload Document")

    uploaded_file = st.file_uploader(

        "Upload PDF or DOCX",

        type=["pdf", "docx"]

    )

    if uploaded_file:

        st.info(uploaded_file.name)

        if st.button("Upload"):

            files = {

                "file": (

                    uploaded_file.name,

                    uploaded_file.getvalue()

                )

            }

            data = {

                "user_id": st.session_state.user_id

            }

            response = requests.post(

                BASE_URL + "/upload",

                files=files,

                data=data

            )

            result = response.json()

            if response.status_code == 200:

                st.success(result["message"])

            else:

                st.error(result["error"])

    st.divider()

    st.subheader("Ask Questions")

    question = st.text_area(

        "Enter your question"

    )

    if st.button("Ask AI"):

        if question == "":

            st.warning("Please enter a question.")

        else:

            response = requests.post(

                BASE_URL + "/query",

                json={

                    "user_id": st.session_state.user_id,

                    "question": question

                }

            )

            result = response.json()

            st.subheader("Answer")

            st.success(result["answer"])

            st.subheader("Source Documents")

            if len(result["sources"]) == 0:

                st.write("No source found.")

            else:

                for source in result["sources"]:

                    st.write(f"{source}")

    st.divider()

    if st.button("Logout"):

        st.session_state.clear()

        st.rerun()
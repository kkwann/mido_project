import streamlit as st

def home():
    st.title("Home")
    st.write("Welcome to the Streamlit application.")
    if 'username' in st.session_state:
        st.success(f"Logged in as {st.session_state['username']}")


import streamlit as st

def home():
    st.title("미도플러스")
    st.title("Home")
    st.write("Welcome to the Mido Webservice.")
    if 'username' in st.session_state:
        st.success(f"Logged in as {st.session_state['username']}")
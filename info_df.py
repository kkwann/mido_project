import streamlit as st
from utils import get_dataframe_from_bigquery

def info_ser_df():
    st.subheader("인포21C 용역입찰 데이터")
    # st.title("인포21C 용역입찰 데이터")
    if 'logged_in' in st.session_state and st.session_state['logged_in']:
        data = get_dataframe_from_bigquery('info21', 'info_df')
        st.write(data)
    else:
        st.warning("Please login to access this page.")
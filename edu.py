import streamlit as st
from utils import get_dataframe_from_bigquery

def edu_budget_df():
    st.subheader("교육청 예산서")
    # st.title("오더리스트")
    if 'logged_in' in st.session_state and st.session_state['logged_in']:
        data = get_dataframe_from_bigquery('edu', 'edu_budget')
        st.write(data)
    else:
        st.warning("Please login to access this page.")
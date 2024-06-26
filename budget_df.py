import streamlit as st
from utils import get_dataframe_from_bigquery

def budget_df():
    st.title("지자체 세부사업별 예산서")
    if 'logged_in' in st.session_state and st.session_state['logged_in']:
        data = get_dataframe_from_bigquery('budget', 'budget_df_today')
        st.write(data)
    else:
        st.warning("Please login to access this page.")
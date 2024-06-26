import streamlit as st
from utils import get_dataframe_from_bigquery

def new_daily():
    st.title("최신 뉴스 기사 스크랩")
    if 'logged_in' in st.session_state and st.session_state['logged_in']:
        data = get_dataframe_from_bigquery('mido_test', 'news_daily')
        st.write(data)
    else:
        st.warning("Please login to access this page.")

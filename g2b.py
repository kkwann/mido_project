import streamlit as st
from utils import get_dataframe_from_bigquery

def shop_detail_df():
    st.subheader("종합쇼핑몰 납품상세내역")
    # st.title("지자체 예산서 링크")
    if 'logged_in' in st.session_state and st.session_state['logged_in']:
        data = get_dataframe_from_bigquery('g2b', 'shop_detail_df_all')
        st.write(data)
    else:
        st.warning("Please login to access this page.")
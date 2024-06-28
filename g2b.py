import streamlit as st
from utils import get_dataframe_from_bigquery
from utils import get_bigquery_client


def shop_detail_df():
    st.subheader("종합쇼핑몰 납품상세내역")
    # st.title("지자체 예산서 링크")
    if 'logged_in' in st.session_state and st.session_state['logged_in']:
        tables = get_bigquery_client().list_tables(f"{'mido-project-426906'}.{'g2b'}")
        table_list = [table.table_id for table in tables if 'shop_detail_df' in table.table_id]

        all_shop_df = []
        for tb_nm in table_list:
            data = get_dataframe_from_bigquery('g2b', tb_nm)
            all_shop_df.extend(data)
            
        st.write(all_shop_df)
    else:
        st.warning("Please login to access this page.")
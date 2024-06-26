import streamlit as st
from utils import get_dataframe_from_bigquery, save_data_to_new_table

def edit_orderlist():
    st.title("Edit Order List")
    if 'logged_in' in st.session_state and st.session_state['logged_in']:
        data = get_dataframe_from_bigquery('mido_test', 'orderlist')
        
        # 데이터 편집
        edited_data = st.experimental_data_editor(data)
        
        if st.button("Save"):
            # 데이터 저장 로직
            save_data_to_new_table(edited_data, 'mido_test', 'modified_orderlist')
            st.success("Changes saved and uploaded to a new BigQuery table!")
    else:
        st.warning("Please login to access this page.")
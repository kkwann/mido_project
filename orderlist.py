import streamlit as st
from utils import get_dataframe_from_bigquery

def orderlist():
    st.subheader("오더리스트")
    # st.title("오더리스트")
    if 'logged_in' in st.session_state and st.session_state['logged_in']:
        data = get_dataframe_from_bigquery('mido_test', 'orderlist')
        
        st.write(f"오더리스트 : {len(data)} 건")
        st.write(data)
    else:
        st.warning("Please login to access this page.")
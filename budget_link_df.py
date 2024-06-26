<<<<<<< HEAD
<<<<<<< HEAD
import streamlit as st
from utils import get_dataframe_from_bigquery

def budget_link_df():
    st.title("지자체 예산서 링크")
    if 'logged_in' in st.session_state and st.session_state['logged_in']:
        data = get_dataframe_from_bigquery('mido_test', 'budget_link_df')
        st.write(data)
    else:
        st.warning("Please login to access this page.")
=======
import streamlit as st
from utils import get_dataframe_from_bigquery

def budget_link_df():
    st.title("지자체 예산서 링크")
    if 'logged_in' in st.session_state and st.session_state['logged_in']:
        data = get_dataframe_from_bigquery('mido_test', 'budget_link_df')
        st.write(data)
    else:
        st.warning("Please login to access this page.")
>>>>>>> origin/main
=======
import streamlit as st
from utils import get_dataframe_from_bigquery

def budget_link_df():
    st.title("지자체 예산서 링크")
    if 'logged_in' in st.session_state and st.session_state['logged_in']:
        data = get_dataframe_from_bigquery('mido_test', 'budget_link_df')
        st.write(data)
    else:
        st.warning("Please login to access this page.")
>>>>>>> origin/main

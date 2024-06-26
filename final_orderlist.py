<<<<<<< HEAD
<<<<<<< HEAD
import streamlit as st
from utils import load_data

def final_orderlist():
    st.title("Final Order List")
    if 'logged_in' in st.session_state and st.session_state['logged_in']:
        data = load_data('mido_test', 'modified_orderlist')
        st.write(data)
    else:
        st.warning("Please login to access this page.")
=======
import streamlit as st
from utils import load_data

def final_orderlist():
    st.title("Final Order List")
    if 'logged_in' in st.session_state and st.session_state['logged_in']:
        data = load_data('mido_test', 'modified_orderlist')
        st.write(data)
    else:
        st.warning("Please login to access this page.")
>>>>>>> origin/main
=======
import streamlit as st
from utils import load_data

def final_orderlist():
    st.title("Final Order List")
    if 'logged_in' in st.session_state and st.session_state['logged_in']:
        data = load_data('mido_test', 'modified_orderlist')
        st.write(data)
    else:
        st.warning("Please login to access this page.")
>>>>>>> origin/main

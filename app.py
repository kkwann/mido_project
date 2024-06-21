import streamlit as st
import pandas as pd
from google.cloud import bigquery
from google.oauth2 import service_account
import json

# GCP 서비스 계정 자격 증명 로드
def get_credentials():
    service_account_info = json.loads(st.secrets["gcp_service_account"])
    credentials = service_account.Credentials.from_service_account_info(service_account_info)
    return credentials

# BigQuery 클라이언트 생성
def get_bigquery_client():
    credentials = get_credentials()
    client = bigquery.Client(credentials=credentials, project=credentials.project_id)
    return client

# 데이터 가져오기
def load_data(table_name):
    client = get_bigquery_client()
    query = f"SELECT * FROM `mido_test.{table_name}`"
    data = client.query(query).to_dataframe()
    return data

# 로그인 기능
def login(users):
    st.subheader("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type='password')
    if st.button("Login"):
        user = users[(users['username'] == username) & (users['password'] == password)]
        if not user.empty:
            st.session_state['logged_in'] = True
            st.session_state['username'] = username
            st.success("Login successful!")
        else:
            st.error("Invalid username or password")

# 홈 화면
def home():
    st.title("Home")
    st.write("Welcome to the Streamlit application.")
    users = load_data('users')
    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False

    if not st.session_state['logged_in']:
        login(users)
    else:
        st.success(f"Logged in as {st.session_state['username']}")

# 오더리스트 화면
def orderlist():
    st.title("Order List")
    if st.session_state.get('logged_in'):
        data = load_data('orderlist')
        st.write(data)
    else:
        st.warning("Please login to access this page.")

# 오더리스트 수정 화면
def edit_orderlist():
    st.title("Edit Order List")
    if st.session_state.get('logged_in'):
        data = load_data('orderlist')
        edited_data = st.experimental_data_editor(data)
        if st.button("Save"):
            # 여기에서 데이터를 BigQuery에 저장하는 코드를 작성합니다.
            st.success("Changes saved!")
    else:
        st.warning("Please login to access this page.")

# 오더리스트 최종 화면
def final_orderlist():
    st.title("Final Order List")
    if st.session_state.get('logged_in'):
        data = load_data('orderlist')
        st.write(data)
    else:
        st.warning("Please login to access this page.")

# 메인 함수
def main():
    st.sidebar.title("Navigation")
    options = st.sidebar.radio("Go to", ["Home", "Order List", "Edit Order List", "Final Order List"])

    if options == "Home":
        home()
    elif options == "Order List":
        orderlist()
    elif options == "Edit Order List":
        edit_orderlist()
    elif options == "Final Order List":
        final_orderlist()

if __name__ == "__main__":
    main()

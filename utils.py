import streamlit as st
from google.cloud import bigquery
from google.oauth2 import service_account

def get_credentials():
    service_account_info = st.secrets["gcp_service_account"]
    credentials = service_account.Credentials.from_service_account_info(service_account_info)
    return credentials

def get_bigquery_client():
    credentials = get_credentials()
    client = bigquery.Client(credentials=credentials, project=credentials.project_id)
    return client

def save_dataframe_to_bigquery(df, dataset_id, table_id):
    # BigQuery 클라이언트 객체 생성
    client = get_bigquery_client()

    # 테이블 레퍼런스 생성
    table_ref = client.dataset(dataset_id).table(table_id)

    # 데이터프레임을 BigQuery 테이블에 적재
    job_config = bigquery.LoadJobConfig()
    job_config.write_disposition = "WRITE_TRUNCATE"  # 기존 테이블 내용 삭제 후 삽입

    job = client.load_table_from_dataframe(df, table_ref, job_config=job_config)
    job.result()  # 작업 완료 대기

    print(f"Data inserted into table {table_id} successfully.")

def get_dataframe_from_bigquery(dataset_id, table_id):
    # BigQuery 클라이언트 생성
    client = get_bigquery_client()

    # 테이블 레퍼런스 생성
    table_ref = client.dataset(dataset_id).table(table_id)

    # 테이블 데이터를 DataFrame으로 변환
    df = client.list_rows(table_ref).to_dataframe()

    return df

def save_data_to_bigquery(dataframe, dataset_id, table_name):
    """
    수정된 데이터를 BigQuery 테이블에 추가합니다.
    Args:
    dataframe (pd.DataFrame): 저장할 데이터가 포함된 Pandas DataFrame
    dataset_id (str): 데이터셋 ID
    table_name (str): 테이블 이름
    """
    client = get_bigquery_client()
    table_ref = f"{dataset_id}.{table_name}"

    job_config = bigquery.LoadJobConfig(write_disposition="WRITE_APPEND")
    job = client.load_table_from_dataframe(dataframe, table_ref, job_config=job_config)
    job.result()  # 작업 완료 대기

    st.write(f"Data uploaded successfully to BigQuery table: {table_ref}.")

def save_data_to_new_table(dataframe, dataset_id, table_name):
    """
    수정된 데이터를 새로운 BigQuery 테이블에 저장합니다.
    Args:
    dataframe (pd.DataFrame): 저장할 데이터가 포함된 Pandas DataFrame
    dataset_id (str): 데이터셋 ID
    table_name (str): 새 테이블 이름
    """
    client = get_bigquery_client()
    table_ref = f"{dataset_id}.{table_name}"

    job_config = bigquery.LoadJobConfig(write_disposition="WRITE_TRUNCATE")
    job = client.load_table_from_dataframe(dataframe, table_ref, job_config=job_config)
    job.result()  # 작업 완료 대기

    st.write(f"Data uploaded successfully to new BigQuery table: {table_ref}.")

def login(users_df):
    st.subheader("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type='password')
    
    if st.button("Login"):
        user = users_df[(users_df['employeeName'] == username) & (users_df['password'] == password)]
        if not user.empty:
            st.session_state['logged_in'] = True
            st.session_state['username'] = username
            st.success("Login successful!")
        else:

import streamlit as st
from google.cloud import bigquery
from google.oauth2 import service_account

def get_credentials():
    service_account_info = st.secrets["gcp_service_account"]
    credentials = service_account.Credentials.from_service_account_info(service_account_info)
    return credentials

def get_bigquery_client():
    credentials = get_credentials()
    client = bigquery.Client(credentials=credentials, project=credentials.project_id)
    return client

def save_dataframe_to_bigquery(df, dataset_id, table_id):
    # BigQuery 클라이언트 객체 생성
    client = get_bigquery_client()

    # 테이블 레퍼런스 생성
    table_ref = client.dataset(dataset_id).table(table_id)

    # 데이터프레임을 BigQuery 테이블에 적재
    job_config = bigquery.LoadJobConfig()
    job_config.write_disposition = "WRITE_TRUNCATE"  # 기존 테이블 내용 삭제 후 삽입

    job = client.load_table_from_dataframe(df, table_ref, job_config=job_config)
    job.result()  # 작업 완료 대기

    print(f"Data inserted into table {table_id} successfully.")

def get_dataframe_from_bigquery(dataset_id, table_id):
    # BigQuery 클라이언트 생성
    client = get_bigquery_client()

    # 테이블 레퍼런스 생성
    table_ref = client.dataset(dataset_id).table(table_id)

    # 테이블 데이터를 DataFrame으로 변환
    df = client.list_rows(table_ref).to_dataframe()

    return df

def save_data_to_bigquery(dataframe, dataset_id, table_name):
    """
    수정된 데이터를 BigQuery 테이블에 추가합니다.
    Args:
    dataframe (pd.DataFrame): 저장할 데이터가 포함된 Pandas DataFrame
    dataset_id (str): 데이터셋 ID
    table_name (str): 테이블 이름
    """
    client = get_bigquery_client()
    table_ref = f"{dataset_id}.{table_name}"

    job_config = bigquery.LoadJobConfig(write_disposition="WRITE_APPEND")
    job = client.load_table_from_dataframe(dataframe, table_ref, job_config=job_config)
    job.result()  # 작업 완료 대기

    st.write(f"Data uploaded successfully to BigQuery table: {table_ref}.")

def save_data_to_new_table(dataframe, dataset_id, table_name):
    """
    수정된 데이터를 새로운 BigQuery 테이블에 저장합니다.
    Args:
    dataframe (pd.DataFrame): 저장할 데이터가 포함된 Pandas DataFrame
    dataset_id (str): 데이터셋 ID
    table_name (str): 새 테이블 이름
    """
    client = get_bigquery_client()
    table_ref = f"{dataset_id}.{table_name}"

    job_config = bigquery.LoadJobConfig(write_disposition="WRITE_TRUNCATE")
    job = client.load_table_from_dataframe(dataframe, table_ref, job_config=job_config)
    job.result()  # 작업 완료 대기

    st.write(f"Data uploaded successfully to new BigQuery table: {table_ref}.")

def login(users_df):
    st.subheader("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type='password')
    
    if st.button("Login"):
        user = users_df[(users_df['employeeName'] == username) & (users_df['password'] == password)]
        if not user.empty:
            st.session_state['logged_in'] = True
            st.session_state['username'] = username
            st.success("Login successful!")
        else:

import streamlit as st
from google.cloud import bigquery
from google.oauth2 import service_account

def get_credentials():
    service_account_info = st.secrets["gcp_service_account"]
    credentials = service_account.Credentials.from_service_account_info(service_account_info)
    return credentials

def get_bigquery_client():
    credentials = get_credentials()
    client = bigquery.Client(credentials=credentials, project=credentials.project_id)
    return client

def save_dataframe_to_bigquery(df, dataset_id, table_id):
    # BigQuery 클라이언트 객체 생성
    client = get_bigquery_client()

    # 테이블 레퍼런스 생성
    table_ref = client.dataset(dataset_id).table(table_id)

    # 데이터프레임을 BigQuery 테이블에 적재
    job_config = bigquery.LoadJobConfig()
    job_config.write_disposition = "WRITE_TRUNCATE"  # 기존 테이블 내용 삭제 후 삽입

    job = client.load_table_from_dataframe(df, table_ref, job_config=job_config)
    job.result()  # 작업 완료 대기

    print(f"Data inserted into table {table_id} successfully.")

def get_dataframe_from_bigquery(dataset_id, table_id):
    # BigQuery 클라이언트 생성
    client = get_bigquery_client()

    # 테이블 레퍼런스 생성
    table_ref = client.dataset(dataset_id).table(table_id)

    # 테이블 데이터를 DataFrame으로 변환
    df = client.list_rows(table_ref).to_dataframe()

    return df

def save_data_to_bigquery(dataframe, dataset_id, table_name):
    """
    수정된 데이터를 BigQuery 테이블에 추가합니다.
    Args:
    dataframe (pd.DataFrame): 저장할 데이터가 포함된 Pandas DataFrame
    dataset_id (str): 데이터셋 ID
    table_name (str): 테이블 이름
    """
    client = get_bigquery_client()
    table_ref = f"{dataset_id}.{table_name}"

    job_config = bigquery.LoadJobConfig(write_disposition="WRITE_APPEND")
    job = client.load_table_from_dataframe(dataframe, table_ref, job_config=job_config)
    job.result()  # 작업 완료 대기

    st.write(f"Data uploaded successfully to BigQuery table: {table_ref}.")

def save_data_to_new_table(dataframe, dataset_id, table_name):
    """
    수정된 데이터를 새로운 BigQuery 테이블에 저장합니다.
    Args:
    dataframe (pd.DataFrame): 저장할 데이터가 포함된 Pandas DataFrame
    dataset_id (str): 데이터셋 ID
    table_name (str): 새 테이블 이름
    """
    client = get_bigquery_client()
    table_ref = f"{dataset_id}.{table_name}"

    job_config = bigquery.LoadJobConfig(write_disposition="WRITE_TRUNCATE")
    job = client.load_table_from_dataframe(dataframe, table_ref, job_config=job_config)
    job.result()  # 작업 완료 대기

    st.write(f"Data uploaded successfully to new BigQuery table: {table_ref}.")

def login(users_df):
    st.subheader("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type='password')
    
    if st.button("Login"):
        user = users_df[(users_df['employeeName'] == username) & (users_df['password'] == password)]
        if not user.empty:
            st.session_state['logged_in'] = True
            st.session_state['username'] = username
            st.success("Login successful!")
        else:
            st.error("Invalid username or password")
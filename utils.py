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

def load_data(dataset_id, table_name):
    """
    BigQuery에서 데이터를 로드하여 Pandas DataFrame으로 반환.
    Args:
    dataset_id (str): 데이터셋 ID
    table_name (str): 테이블 이름
    """
    # BigQuery 클라이언트 생성
    try:
        client = get_bigquery_client()

        query = f"SELECT * FROM `{dataset_id}.{table_name}`"
        data = client.query(query).to_dataframe()

        # # 테이블 레퍼런스 생성 --> 데이터양 많을때 성능 떨어짐
        # table_ref = client.dataset(dataset_id).table(table_name) 

        # # table = client.get_table(table_ref) # API 요청

        # # 테이블 데이터를 DataFrame으로 변환
        # data = client.list_rows(table_ref).to_dataframe()
        return data
    
    except Exception as e:
        st.error(f"Error loading data from BigQuery: {e}")
        raise

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
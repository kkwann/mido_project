import streamlit as st
from utils import get_dataframe_from_bigquery

def shop_detail_df():
    st.subheader("종합쇼핑몰 납품상세내역")
    # st.title("지자체 예산서 링크")
    if 'logged_in' in st.session_state and st.session_state['logged_in']:

        data = get_dataframe_from_bigquery('g2b', 'shop_detail_df_all')
        data = data[['납품요구접수일자', '수요기관명', '납품요구건명', '업체명', '단가', '단위', '수량', '금액', '수요기관구분', '수요기관지역명','납품요구지청명']]
        data = data.sort_values(['납품요구접수일자'],ascending=False).reset_index(drop=True)

        st.write(f"종합쇼핑몰 납품상세내역 데이터 : {len(data)} 건")
        st.write(data)
    else:
        st.warning("Please login to access this page.")
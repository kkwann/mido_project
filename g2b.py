import streamlit as st
from datetime import datetime, timedelta
from utils import get_dataframe_from_bigquery

# 오늘 날짜
today = datetime.today()#.strftime('%Y%m%d')

# 어제 날짜 계산
ytday = datetime.today() - timedelta(days=1)

# 만약 어제, 오늘이 토요일(5) 또는 일요일(6)이라면, 그 전주 금요일로 변경
if ytday.weekday() == 5:  # 토요일
    ytday -= timedelta(days=1)
elif ytday.weekday() == 6:  # 일요일
    ytday -= timedelta(days=2)
if today.weekday() == 5:  # 토요일
    today -= timedelta(days=1)
elif today.weekday() == 6:  # 일요일
    today -= timedelta(days=2)

# 'YYYYMMDD' 형식으로 변환
ytday = ytday.strftime('%Y%m%d')
today = today.strftime('%Y%m%d')

years = today[:-4]

def shop_detail_df():
    st.subheader("종합쇼핑몰 납품상세내역")
    
    if 'logged_in' in st.session_state and st.session_state['logged_in']:

        data = get_dataframe_from_bigquery('g2b', 'shop_detail_df_all')
        data = data[data['납품요구접수일자'].str.split('-').str[0]==years].reset_index(drop=True)
        data = data[['납품요구접수일자', '수요기관명', '납품요구건명', '업체명', '단가', '단위', '수량', '금액', '수요기관구분', '수요기관지역명','납품요구지청명']]
        data = data.sort_values(['납품요구접수일자'],ascending=False).reset_index(drop=True)
        
        st.write(f"종합쇼핑몰 납품상세내역 데이터 : {len(data)} 건")
        st.write(data)
    else:
        st.warning("Please login to access this page.")
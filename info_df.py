import streamlit as st
from streamlit_option_menu import option_menu
from utils import get_dataframe_from_bigquery
from datetime import datetime, timedelta

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

data_con = get_dataframe_from_bigquery('info21', 'bid_con_df_0' + today[4:6])
data_ser = get_dataframe_from_bigquery('info21', 'bid_ser_df_0' + today[4:6])
data_pur = get_dataframe_from_bigquery('info21', 'bid_pur_df_0' + today[4:6])


def info_df():
    st.subheader("인포21C 입찰 데이터")

    if 'logged_in' in st.session_state and st.session_state['logged_in']:
        sub_option = option_menu(None, ["공사입찰", "용역입찰", "구매입찰"], 
                                 icons=['archive', 'archive', 'archive'], 
                                 menu_icon="cast", default_index=0, orientation="horizontal")
        
        if sub_option == "공사입찰":
            st.write(f"금일 인포21 공사입찰 데이터 : {len(data_con)} 건")
            st.dataframe(data_con)

        elif sub_option == "용역입찰":
            st.write(f"금일 인포21 용역입찰 데이터 : {len(data_ser)} 건")
            st.dataframe(data_ser)
            
        elif sub_option == "구매입찰":
            st.write(f"금일 인포21 구매입찰 데이터 : {len(data_pur)} 건")
            st.dataframe(data_pur)

    else:
        st.warning("Please login to access this page.")
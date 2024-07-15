import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
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

# today = datetime.today().strftime('%Y%m%d')
# ytday = (datetime.today() - timedelta(days=1)).strftime('%Y%m%d')

data_listup = get_dataframe_from_bigquery('budget', 'budget_df_listup')
data_new = get_dataframe_from_bigquery('budget', 'budget_df_new')
data_delete = get_dataframe_from_bigquery('budget', 'budget_df_delete')

def search_and_display_data(data):
    # st.write(f"Displaying {data_tb}")
    
    keyword = st.text_input(f"세부사업명에서 찾고 싶은 키워드를 입력해주세요.")
    
    # Replace 'your_dataframe' with the actual DataFrame variable or function
    # data = get_dataframe_from_bigquery('budget', data_tb)
    
    # 날짜 형식 변환
    data['집행일자'] = data['집행일자'].astype(str)
    data['회계연도'] = data['회계연도'].astype(str)

    # 인조잔디 우선 정렬
    data = pd.concat([data[data['세부사업명'].str.contains('인조잔디')],
                      data[~data['세부사업명'].str.contains('인조잔디')]],axis=0).reset_index(drop=True)

    if keyword:
        filtered_data = data[data['세부사업명'].str.contains(keyword)]
        # filtered_data = data[data.apply(lambda row: row.astype(str).str.contains(keyword).any(), axis=1)]
        # st.write(filtered_data)
        st.dataframe(filtered_data)

    else:
        # st.write(data)
        st.dataframe(data)

def budget_df():
    st.subheader("지자체 세부사업별 예산서")
    if 'logged_in' in st.session_state and st.session_state['logged_in']:
        sub_option = option_menu(None, ["기존데이터", "추가데이터", "종료데이터"], 
                                icons=['archive', 'plus', 'x'], 
                                menu_icon="cast", default_index=0, orientation="horizontal")
        
        if sub_option == "기존데이터":
            st.write(f"금일 지자체 세부사업별 데이터 : {len(data_listup)} 건")
            search_and_display_data(data_listup)
        elif sub_option == "추가데이터":
            st.write(f"금일 추가된 지자체 세부사업별 데이터 : {len(data_new)} 건")
            search_and_display_data(data_new)
        elif sub_option == "종료데이터":
            st.write(f"금일 종료된 지자체 세부사업별 데이터 : {len(data_delete)} 건")
            search_and_display_data(data_delete)
    
    else:
        st.warning("Please login to access this page.")


    # st.title("지자체 세부사업별 예산서")
    # if 'logged_in' in st.session_state and st.session_state['logged_in']:
    #     data = get_dataframe_from_bigquery('budget', 'budget_df_today')
    #     st.write(data)
    # else:
    #     st.warning("Please login to access this page.")
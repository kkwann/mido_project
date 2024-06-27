import streamlit as st
from streamlit_option_menu import option_menu
from utils import get_dataframe_from_bigquery

def search_and_display_data(data_tb):
    # st.write(f"Displaying {data_tb}")
    
    keyword = st.text_input(f"세부사업명에서 찾고 싶은 키워드를 입력해주세요.")
    
    # Replace 'your_dataframe' with the actual DataFrame variable or function
    data = get_dataframe_from_bigquery('budget', data_tb)
    
    # 날짜 형식으로 변환
    data['집행일자'] = pd.to_datetime(data['집행일자'], format='%Y%m%d', errors='coerce')

    if keyword:
        filtered_data = data[data['세부사업명'].str.contains(keyword)]
        # filtered_data = data[data.apply(lambda row: row.astype(str).str.contains(keyword).any(), axis=1)]
        st.write(filtered_data)
    else:
        st.write(data)

def budget_df():
    st.subheader("지자체 세부사업별 예산서")
    if 'logged_in' in st.session_state and st.session_state['logged_in']:
        sub_option = option_menu(None, ["기존데이터", "추가데이터", "종료데이터"], 
                                icons=['archive', 'plus', 'x'], 
                                menu_icon="cast", default_index=0, orientation="horizontal")
        
        if sub_option == "기존데이터":
            st.write(f"금일 지자체 세부사업별 데이터")
            search_and_display_data('budget_df_020240627')
        elif sub_option == "추가데이터":
            st.write(f"금일 추가된 지자체 세부사업별 데이터")
            search_and_display_data("budget_df_020240627")
        elif sub_option == "종료데이터":
            st.write(f"금일 종료된 지자체 세부사업별 데이터")
            search_and_display_data("budget_df_020240627")
    
    else:
        st.warning("Please login to access this page.")


    # st.title("지자체 세부사업별 예산서")
    # if 'logged_in' in st.session_state and st.session_state['logged_in']:
    #     data = get_dataframe_from_bigquery('budget', 'budget_df_today')
    #     st.write(data)
    # else:
    #     st.warning("Please login to access this page.")
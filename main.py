import streamlit as st
from streamlit_option_menu import option_menu
from utils import get_dataframe_from_bigquery
from home import home

from orderlist import orderlist
# from edit_orderlist import edit_orderlist
# from final_orderlist import final_orderlist

from budget_df import budget_df
from budget_link_df import budget_link_df

from g2b import shop_detail_df

from info_df import info_ser_df

from news_daily import news_daily

def main():
    # st.title("미도플러스")

    # 세션 상태에서 로그인 상태 확인 및 초기화
    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False
        st.session_state['username'] = None
        st.session_state['password'] = None

    # 로그인 처리
    if not st.session_state['logged_in']:
        st.subheader("Login")
        username = st.text_input("Username")
        password = st.text_input("Password", type='password')
        
        if st.button("Login"):
            try:
                # 'users' 테이블에서 사용자 정보 로드
                users = get_dataframe_from_bigquery('mido_test', 'users')
                user = users[(users['employeeName'] == username) & (users['password'] == password)]
                
                if not user.empty:
                    st.session_state['logged_in'] = True
                    st.session_state['username'] = username
                    st.session_state['password'] = password
                    st.success("Login successful!")
                    st.experimental_rerun()
                    
                else:
                    st.error("Invalid username or password")
            except Exception as e:
                st.error(f"Error during login: {e}")

    # 로그인 성공 후 네비게이션 메뉴 제공
    if st.session_state['logged_in']:
        st.sidebar.title("제공 서비스")

        st.sidebar.write(f"Logged in as: {st.session_state['username']}")
        if st.sidebar.button("Logout"):
            st.session_state['logged_in'] = False
            st.session_state['username'] = None
            st.session_state['password'] = None
            st.experimental_rerun()

        with st.sidebar:
            option = option_menu("Menu", 
                                 ["Home", "오더리스트", "지자체 예산서 링크", "지자체 예산서", "종합쇼핑몰 납품상세내역","인포21", "뉴스 스크랩"], 
                                icons=['house', 'list', '🔗', 'book', '🛒','info', 'newspaper'], 
                                menu_icon="cast", default_index=0, orientation="vertical", key="sidebar_menu",
                                styles={
                                    "container": {"padding": "5!important", "background-color": "#fafafa", "color": "black"},
                                    "icon": {"color": "orange", "font-size": "25px"}, 
                                    "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee", "color": "black"},
                                    "nav-link-selected": {"background-color": "#02ab21", "color": "black"},
                                    }
                                )
        
        if option == "Home":
            home()
        elif option == "오더리스트":
            orderlist()

        elif option == "지자체 예산서 링크":
            budget_link_df()

        elif option == "지자체 예산서":
            budget_df()

        elif option == "종합쇼핑몰 납품상세내역":
            shop_detail_df()

        elif option == "인포21":
            info_ser_df()

        elif option == "뉴스 스크랩":
            news_daily()

if __name__ == "__main__":
    main()
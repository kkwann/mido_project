import streamlit as st
from home import home
from orderlist import orderlist
from edit_orderlist import edit_orderlist
from final_orderlist import final_orderlist
from utils import load_data

def main():
    st.title("Streamlit Application")

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
                users = load_data('mido_test', 'users')
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
        st.sidebar.title("DB")
        data = load_data('mido_test', 'orderlist')
        st.write(data)

if __name__ == "__main__":
    main()

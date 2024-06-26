import streamlit as st
from streamlit_option_menu import option_menu
from utils import get_dataframe_from_bigquery

def search_and_display_data(data_type):
    st.write(f"Displaying {data_type}")
    
    keyword = st.text_input(f"Search {data_type} by keyword")
    
    # Replace 'your_dataframe' with the actual DataFrame variable or function
    data = get_dataframe_from_bigquery('budget', 'budget_df_today')
    
    if keyword:
        filtered_data = data[data.apply(lambda row: row.astype(str).str.contains(keyword).any(), axis=1)]
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
            search_and_display_data("기존데이터")
        elif sub_option == "추가데이터":
            search_and_display_data("추가데이터")
        elif sub_option == "종료데이터":
            search_and_display_data("종료데이터")
    
    else:
        st.warning("Please login to access this page.")


    # st.title("지자체 세부사업별 예산서")
    # if 'logged_in' in st.session_state and st.session_state['logged_in']:
    #     data = get_dataframe_from_bigquery('budget', 'budget_df_today')
    #     st.write(data)
    # else:
    #     st.warning("Please login to access this page.")
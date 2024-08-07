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

def news_daily():
    st.subheader("최신 뉴스 기사 스크랩")
    
    if 'logged_in' in st.session_state and st.session_state['logged_in']:
        data = get_dataframe_from_bigquery('news', 'news_daily_listup')
        data = data.sort_values(['기사날짜'],ascending=False).reset_index(drop=True)
        
        st.write(f"최신 뉴스 기사 데이터 : {len(data)} 건")
        st.data_editor(
            data[['기사날짜','원본링크','제목','본문']],
            column_config={
                "원본링크": st.column_config.LinkColumn(
                    "원본링크",
                    display_text="Link",
                    help="기사의 원본 링크",
                    validate="^https?://",
                    max_chars=100)
                    },
                    hide_index=True,
                    )
        
        # st.write(data)
    else:
        st.warning("Please login to access this page.")
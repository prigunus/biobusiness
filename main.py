import streamlit as st
from streamlit_option_menu import option_menu
import subpage_1, subpage_4

st.title("바이오사업본부")
st.set_page_config(layout="wide")


# 슬라이드 메뉴
with st.sidebar:
    choice = option_menu("KTC", ["매출관련", "TODO", "기관운영", "인력관리", "주요소식", "시장에측"],
                         icons=['house', 'kanban', 'bi bi-robot'],
                         menu_icon="app-indicator", default_index=0,
                         styles={
        "container": {"padding": "4!important", "background-color": "#fafafa"},
        "icon": {"color": "black", "font-size": "25px"},
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#fafafa"},
        "nav-link-selected": {"background-color": "#08c7b4"},
    }
    )
    
    
if choice == '매출관련':
    st.subheader('본부 작년대비 실적')
    subpage_1.sub1_front()
    
elif choice == '인력관리':
    st.subheader('인력관리')
    subpage_4.sub1_front()
    
    
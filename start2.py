import streamlit as st


st.set_page_config(layout="wide")
st.title("전자의료센터")
st.button("조회", on_click=search.refer_fun)



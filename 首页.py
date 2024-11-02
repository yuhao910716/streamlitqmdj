import streamlit as st
import leafmap.foliumap as leafmap
from streamlit_option_menu import option_menu

import streamlit as st
# from streamlit_option_menu import option_menu
st.set_page_config(page_title="浩浩奇门遁甲", page_icon="☯️☯️️☯️", layout="wide")
st.audio("./音乐/qm1.mp3")

c1, c2,c3 = st.columns([1,1,1])
with c2:
    st.title('奇门遁甲十二生肖')
col1, col2,col3,col4,col5,col6 = st.columns([1,1,1,1,1,1])
with col1:
    st.image("./图片/1.png")

with col2:
    st.image("./图片/2.png")

with col3:
    st.image("./图片/3.png")

with col4:
    st.image("./图片/4.png")

with col5:
    st.image("./图片/5.png")
#
with col6:
    st.image("./图片/6.png")
# col11, col21,col31,col41,col51,col61 = st.columns([1,1,1,1,1,1])
# with col11:
#     st.image("./图片/7.png")
#
# with col21:
#     st.image("./图片/8.png")
#
# with col31:
#     st.image("./图片/9.png")
#
# with col41:
#     st.image("./图片/10.png")
#
# with col51:
#     st.image("./图片/11.png")
#
# with col61:
#     st.image("./图片/12.png")
#

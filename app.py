
import streamlit as st

st.title("HowLife - 당신의 꾸준함, AI가 함께 만듭니다.")
st.set_page_config(layout="wide")
empty1, con1, empty2=st.columns([0.3,1.0,0.3])
empty1, con2, con3,empty2=st.columns([0.3,0.7,0.3,0.3])
empty1,con4,empty2=st.columns([0.3,1.0,0.3])

with empty1:
      st.empty()

with con1:
      st.header('1')

with con2:
       st.header('2')

with con3:
      st.header('3')

with con4:
      st.header('4')

with empty2:
      st.empty()













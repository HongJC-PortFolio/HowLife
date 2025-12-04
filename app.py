
import streamlit as st

st.title("HowLife - 당신의 꾸준함, AI가 함께 만듭니다.")
st.set_page_config(layout="wide")
empty1, con1, empty2=st.columns([0.3,1.0,0.3])
empty1, con2, con3,empty2=st.columns([0.3,0.7,0.3,0.3])
empty1,con4,empty2=st.columns([0.3,1.0,0.3])

with empty1:
      empty()

with con1:
      st.header('AI의 오늘 행동 제안 ( AI Today Insight )')

with con2:
       st.header('오늘의 목표 - 물 / 영양제 / 운동 요약')

with con3:
      st.header('AI의 전 날 피드백 + 응원과 격려')

with con4:
      st.header('주간 꾸준함')

with empty2:
      empty()













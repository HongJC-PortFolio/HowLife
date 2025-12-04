import streamlit as st

st.title("HowLife - 당신의 꾸준함, AI가 함께 만듭니다.")

tab1,tab2,tab3,tab4=st.tabs(['aiInsight','todayGoals','aiFeedback&Cheers','weekGraph'])

with tab1:
      st.header('AI의 오늘 행동 제안 ( AI Today Insight )')

with tab1:
      st.header('오늘의 목표 - 물 / 영양제 / 운동 요약')

with tab1:
      st.header('AI의 전 날 피드백 + 응원과 격려')

with tab1:
      st.header('주간 꾸준함')

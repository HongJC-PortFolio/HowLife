import streamlit as st

st.title("HowLife - 당신의 꾸준함, AI가 함께 만듭니다.")

tab1,tab2,tab3,tab4=st.tabs(['aiInsight','todayGoals','aiFeedback&Cheers','weekGraph'])

with tab1:
      st.header('AI의 오늘 행동 제안 ( AI Today Insight )')
      st.title('상태 엘리먼트 예제')
      st.success('성공 메시지입니다!', icon="✅")
      st.info('정보성 메시지입니다.', icon="ℹ️")
      st.warning('경고 메시지입니다. 주의가 필요합니다.', icon="⚠️")
      st.error('오류 메시지입니다. 문제가 발생했습니다.', icon="❌")
      st.exception(RuntimeError('런타임 오류가 발생했습니다!'))

with tab2:
      st.header('오늘의 목표 - 물 / 영양제 / 운동 요약')

with tab3:
      st.header('AI의 전 날 피드백 + 응원과 격려')

with tab4:
      st.header('주간 꾸준함')

import streamlit as st
import time

st.title("HowLife - 당신의 꾸준함, AI가 함께 만듭니다.")

tab1,tab2,tab3,tab4=st.tabs(['aiInsight','todayGoals','aiFeedback&Cheers','weekGraph'])

with tab1:
      st.header('AI의 오늘 행동 제안 ( AI Today Insight )')
      st.title('st.toast 예제')
      if st.button('토스트 메시지 표시'):
            st.toast('작업이 성공적으로 완료되었습니다!', icon='🎉') # 아이콘 추가 가능
            time.sleep(1)
            st.toast('다른 알림입니다.')
            time.sleep(1)
            st.toast('마지막 알림입니다!')

with tab2:
      st.header('오늘의 목표 - 물 / 영양제 / 운동 요약')

with tab3:
      st.header('AI의 전 날 피드백 + 응원과 격려')

with tab4:
      st.header('주간 꾸준함')

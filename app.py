
import streamlit as st

st.title("HowLife - 당신의 꾸준함, AI가 함께 만듭니다.")
st.set_page_config(layout="wide")
empty1, con1, empty2=st.columns([0.3,1.0,0.3])
empty1, con2, con3,empty2=st.columns([0.3,0.7,0.3,0.3])
empty1,con4,empty2=st.columns([0.3,1.0,0.3])

with empty1:
      st.empty()

with con1:
      ai_insight_html = """
<div style="
    border: 2px solid #7e7e7e;
    padding: 25px 30px;
    border-radius: 12px;
    margin-top: 20px;
">
    <h3 style="
        text-align: center; 
        margin-bottom: 12px;
        font-weight: 700;
    ">
        AI의 오늘 행동 제안 ( AI Today Insight )
    </h3>

    <p style="
        text-align: center; 
        font-size: 17px;
        margin-top: 5px;
    ">
        Ex) 물 마시지 않은 지 3시간이 지났어요. 목이 건조해지지 않게 물 한 잔 어떠세요?
    </p>
</div>
"""

st.markdown(ai_insight_html, unsafe_allow_html=True)

with con2:
       st.header('2')

with con3:
      st.header('3')

with con4:
      st.header('4')

with empty2:
      st.empty()













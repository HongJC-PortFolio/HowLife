
import streamlit as st

st.title("HowLife - 당신의 꾸준함, AI가 함께 만듭니다.")
st.set_page_config(layout="wide")
empty1, con1, empty2=st.columns([0.3,1.0,0.3])
empty1, con2, con3,empty2=st.columns([0.3,0.7,0.3,0.3])
empty1,con4,empty2=st.columns([0.3,1.0,0.3])

with empty1:
      st.empty()

with con1:
    ai_insight_html = """<div style="
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
</div>"""

st.markdown(ai_insight_html, unsafe_allow_html=True)

with con2:
      st.markdown("""
    <h2 style='text-align:center;'>오늘의 목표<br>- 물 / 영양제 / 운동 요약</h2>
""", unsafe_allow_html=True)

# 전체 컨테이너
with st.container():
    left, right = st.columns([0.55, 0.45])

    # ---------------------------
    # LEFT (물 / 영양제 / 운동)
    # ---------------------------
    with left:
        st.markdown("<div style='padding:10px; border:1px solid #888; border-radius:5px; margin-bottom:15px;'>"
                    "<b>물 : </b>850ml / 2000ml</div>", unsafe_allow_html=True)

        st.markdown("<div style='padding:10px; border:1px solid #888; border-radius:5px; margin-bottom:15px;'>"
                    "<b>영양제 : </b>3 / 5</div>", unsafe_allow_html=True)

        st.markdown("<div style='padding:10px; border:1px solid #888; border-radius:5px;'>"
                    "<b>운동 : </b>25m / 60m</div>", unsafe_allow_html=True)

    # ---------------------------
    # RIGHT (오늘의 통합 목표 달성도)
    # ---------------------------
    with right:
        st.markdown("""
            <div style='text-align:center; padding:15px; border:1px solid #888; border-radius:5px;'>
                <h4>오늘의 통합 목표 달성도</h4>
                <img src="https://cdn-icons-png.flaticon.com/512/616/616408.png" width="120">
            </div>
        """, unsafe_allow_html=True)

with con3:
      st.header('3')

with con4:
      st.header('4')

with empty2:
      st.empty()













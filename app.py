
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
       st.markdown("<br>", unsafe_allow_html=True)

# 큰 박스 전체를 감싸는 틀
today_goal_html = """<div style="
    border: 2px solid #7e7e7e;
    padding: 25px;
    border-radius: 12px;
    margin-top: 20px;
">
    <h3 style="text-align:center; margin-bottom: 20px;">
        오늘의 목표 - 물 / 영양제 / 운동 요약
    </h3>
</div>
"""

# 먼저 틀만 표시
st.markdown(today_goal_html, unsafe_allow_html=True)

# -----------------------------
# 박스 내부에 4개의 칼럼 위치시키기
# (물 / 영양제 / 운동 / 오늘의 달성도)
# -----------------------------
col1, col2, col3, col4 = st.columns([1, 1, 1, 1])

# ★ 1) 물 박스
with col1:
    st.markdown("""
    <div style="
        border: 1.5px solid #b4b4b4;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
    ">
        <h4>물</h4>
        <p>850ml / 2000ml</p>
    </div>
    """, unsafe_allow_html=True)

# ★ 2) 영양제 박스
with col2:
    st.markdown("""
    <div style="
        border: 1.5px solid #b4b4b4;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
    ">
        <h4>영양제</h4>
        <p>3 / 5</p>
    </div>
    """, unsafe_allow_html=True)

# ★ 3) 운동 박스
with col3:
    st.markdown("""
    <div style="
        border: 1.5px solid #b4b4b4;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
    ">
        <h4>운동</h4>
        <p>25m / 60m</p>
    </div>
    """, unsafe_allow_html=True)

# ★ 4) 오늘의 통합 목표 달성도 박스
with col4:
    st.markdown("""
    <div style="
        border: 1.5px solid #b4b4b4;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
    ">
        <h4>오늘의 통합 목표 달성도</h4>
        <p>🌳</p>  <!-- 나중에 tree.png 넣을 예정 -->
    </div>
    """, unsafe_allow_html=True)

with con3:
      st.header('3')

with con4:
      st.header('4')

with empty2:
      st.empty()













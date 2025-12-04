import streamlit as st

# ----------------------------------
# 기본 설정
# ----------------------------------
st.set_page_config(page_title="HowLife 홈", layout="wide")


# ----------------------------------
# 사이드바 메뉴
# ----------------------------------
with st.sidebar:
    st.markdown("""
        <div style="text-align:center; font-size:22px; font-weight:700; margin-bottom:20px;">
            프로필박스<br><br>
            <img src="https://cdn-icons-png.flaticon.com/512/1946/1946429.png" width="80"><br>
            닉네임
        </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### 🏠 홈")
    st.markdown("---")
    st.markdown("### 📘 기록")
    st.markdown("---")
    st.markdown("### 🤖 AI채팅")
    st.markdown("---")
    st.markdown("### 💬 커뮤니티")
    st.markdown("---")
    st.markdown("### ⚙️ 설정")
    st.markdown("---")


# ----------------------------------
# 제목 (HowLife 문구)
# ----------------------------------
st.markdown("""
    <div style="text-align:center; margin-top:10px; margin-bottom:30px;">
        <h2><b>HowLife - 당신의 꾸준함, AI가 함께 만듭니다</b></h2>
    </div>
""", unsafe_allow_html=True)


# ----------------------------------
# AI Today Insight
# ----------------------------------
st.markdown("""
    <div style="
        border: 2px solid #333;
        padding: 20px;
        border-radius: 8px;
        font-size: 18px;
        margin-bottom: 35px;">
        <b>AI의 오늘 행동 제안 (AI Today Insight)</b><br><br>
        Ex) 물 마시지 않은 지 3시간이 지났어요. 목이 건조하지 않게 물 한 잔 어때요?
    </div>
""", unsafe_allow_html=True)


# ----------------------------------
# 오늘의 목표 영역
# ----------------------------------
st.markdown("""
    <h3 style="text-align:center; margin-bottom:20px;">
        오늘의 목표<br>- 물 / 영양제 / 운동 요약 -
    </h3>
""", unsafe_allow_html=True)


goal_container_style = """
    border: 2px solid #333;
    border-radius: 10px;
    padding: 20px;
    margin-bottom: 30px;
"""


st.markdown(f"<div style='{goal_container_style}'>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([0.4, 0.33, 0.27])


# LEFT
with col1:
    small_box = """
        border:2px solid #444; 
        padding:12px; 
        border-radius:6px; 
        margin-bottom:15px; 
        font-size:18px;
    """

    st.markdown(f"<div style='{small_box}'><b>물 :</b> 850ml / 2000ml</div>", unsafe_allow_html=True)
    st.markdown(f"<div style='{small_box}'><b>영양제 :</b> 3 / 5</div>", unsafe_allow_html=True)
    st.markdown(f"<div style='{small_box}'><b>운동 :</b> 25m / 60m</div>", unsafe_allow_html=True)


# CENTER (통합 목표 달성도)
with col2:
    st.markdown("""
        <div style="
            border:2px solid #444;
            padding:20px;
            border-radius:8px;
            text-align:center;
        ">
            <b>오늘의 통합 목표 달성도</b><br><br>
            <img src="https://cdn-icons-png.flaticon.com/512/616/616408.png" width="120">
        </div>
    """, unsafe_allow_html=True)


# RIGHT (전날 피드백)
with col3:
    st.markdown("""
        <div style="
            border:2px solid #444;
            padding:20px;
            border-radius:8px;
            text-align:center;
        ">
            <b>AI의 전 날 피드백<br>+ 응원과 격려</b><br><br>
            <img src="https://cdn-icons-png.flaticon.com/512/2883/2883825.png" width="110">
        </div>
    """, unsafe_allow_html=True)


st.markdown("</div>", unsafe_allow_html=True)   # 오늘의 목표 컨테이너 닫기


# ----------------------------------
# 주간 꾸준함 달력
# ----------------------------------
st.markdown("""
    <div style="
        border: 2px solid #333;
        border-radius: 10px;
        padding: 30px;
        margin-top: 10px;
        margin-bottom: 20px;
        text-align:center;
        font-size:20px;
    ">
        <b>주간 꾸준함 미니 달력 형식</b><br><br>
        <img src="https://cdn-icons-png.flaticon.com/512/747/747310.png" width="120">
    </div>
""", unsafe_allow_html=True)

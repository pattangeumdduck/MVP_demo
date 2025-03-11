import streamlit as st

# 0) 페이지 설정
st.set_page_config(
    page_title="같이 家(가) - 돌봄 프로젝트",
    page_icon="🩺",  # emoji or local image url/base64
    layout="wide"
)

# 1) 배경 이미지 + CSS
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
    background: url("https://via.placeholder.com/1920x1080?text=Background+Image");
    background-size: cover;
    background-position: center;
}
/* 사이드바 투명 (필요 시) 
[data-testid="stSidebar"] > div:first-child {
    background-color: rgba(255, 255, 255, 0.3);
} 
*/
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# 2) 중앙 정렬 타이틀
st.markdown(
    """
    <h1 style='text-align: center; margin-top: 0; padding-top: 10px;'>
        같이 家(가) : 돌봄 프로젝트
    </h1>
    """,
    unsafe_allow_html=True
)

# 3) 소개 섹션
with st.container():
    st.write("""
    ### 소개
    급격한 고령화로 독거노인이 늘어나는 사회에서, 노인과 청년이 한 공간에서 
    상생할 수 있는 ‘돌봄 쉐어하우스 플랫폼’을 제안합니다.  
    \n
    이 프로젝트는 **간단한 돌봄 서비스**를 먼저 제공하여 심리적 장벽을 낮추고, 
    이후에는 **실제 쉐어하우스 매칭**으로 확장될 예정입니다.
    """)

# 4) 하이라이트(장점) 섹션
st.write("---")  # 구분선
st.subheader("프로젝트 핵심 특징")

# 한 행에 3개 열
col1, col2, col3 = st.columns(3)

with col1:
    st.image("https://via.placeholder.com/200?text=Safe", use_container_width=True)
    st.markdown("**안전한 매칭**\n\n사전 신원 검증과 안전장치를 통해 서로 믿고 지낼 수 있습니다.")

with col2:
    st.image("https://via.placeholder.com/200?text=Flexible", use_container_width=True)
    st.markdown("**유연한 돌봄**\n\n간단한 일상 케어부터 복지 서비스 연계까지, 필요에 맞춘 수준별 제공.")

with col3:
    st.image("https://via.placeholder.com/200?text=Community", use_container_width=True)
    st.markdown("**커뮤니티 형성**\n\n노인과 청년의 교류를 통해 세대 간 벽을 허물고, 새로운 공동체 문화를 만듭니다.")

# 5) 팀 소개(또는 개발 인원 소개)
st.write("---")
st.subheader("팀 소개")
tab1, tab2, tab3 = st.tabs(["팀 개요", "연락처", "역할 분담"])

with tab1:
    st.write("""
    저희 팀은 **돌봄 분야**와 **IT 기술**에 관심 있는 청년들이 모여, 
    ‘함께 어울려 사는 사회’를 꿈꾸며 시작했습니다.  
    각자의 전공과 경험을 살려, 노인-청년 매칭 플랫폼을 구상하고 있습니다.
    """)

with tab2:
    st.write("**이메일**: contact@example.com")
    st.write("**전화**: 010-XXXX-XXXX")

with tab3:
    st.write("""
    - 기획/PM: 김지원, 정우석
    - 개발: 주우영  
    - UX/UI 디자인: 이지후  
    """)

# 6) 기능 미리보기: 설문조사 / 매칭 / 돌봄 관리
st.write("---")
st.subheader("주요 기능 미리보기")

feature_cols = st.columns([1, 1, 1])
feature_list = [
    {
        "title": "사전 설문조사",
        "img": "image/친절.png",
        "desc": "간단한 라이프스타일 질문을 통해 기본 정보와 돌봄 필요도를 파악합니다."
    },
    {
        "title": "맞춤 매칭",
        "img": "image/신원확인.jpg",
        "desc": "청년-노인 간 조건이 맞으면, 매칭 알림을 제공하고 대화를 주선합니다."
    },
    {
        "title": "돌봄 대상자 관리",
        "img": "image/돌봄.jpg",
        "desc": "노인 대상자를 등록/삭제하며, 필요한 돌봄 범위를 확인하고 관리할 수 있습니다."
    },
]

for col, feat in zip(feature_cols, feature_list):
    with col:
        st.image(feat["img"], use_container_width=True)
        st.markdown(f"**{feat['title']}**")
        st.write(feat["desc"])

# 7) 이용 안내
st.write("---")
st.subheader("이용 방법")
st.markdown("""
1. **왼쪽 사이드바**의 **Signup**에서 회원가입을 진행 (설문조사 포함 가능)  
2. **Matching** 메뉴에서 로그인 후, 맞춤 매칭을 확인  
3. **CareService** 메뉴에서 돌봄 대상자 등록/삭제 가능  
""")

# 8) 마무리
st.write("---")
st.markdown("""
<div style='text-align: center; font-size: 18px; margin-top: 30px;'>
감사합니다. <br>
보다 나은 상생 문화를 만들어가는 <strong>같이 家(가)</strong> 프로젝트였습니다.
</div>
""", unsafe_allow_html=True)
#adasdfa
st.write("---")

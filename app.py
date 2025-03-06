import streamlit as st

# 페이지 레이아웃 최대 너비 사용 (선택)
st.set_page_config(
    page_title="같이 家(가)",
    page_icon="image/mvp_icon1.png",  
    layout="wide"
)
# 세션 스테이트 초기화 (유저 데이터 저장용)
if "users" not in st.session_state:
    st.session_state["users"] = {}
if "preferences" not in st.session_state:
    st.session_state["preferences"] = {}

# ----- 1) CSS로 배경 이미지 설정 -----
page_bg_img = """
<style>
/* 메인 컨테이너 */
[data-testid="stAppViewContainer"] {
    background: url("image/mvp_home.jpg");
    background-size: cover;
    background-position: center;
}

/* (선택) 사이드바 배경을 투명 또는 다른 색으로 바꾸고 싶다면
[data-testid="stSidebar"] > div:first-child {
    background-color: rgba(0,0,0,0.3);
}
*/
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# ----- 2) 중앙 정렬된 H1 타이틀 -----
st.markdown(
    """
    <h1 style='text-align: center; margin-top: 0;'>
        같이 家(가)
    </h1>
    """,
    unsafe_allow_html=True
)

# ----- 3) 내용 컨테이너 -----
with st.container():
    st.header("Who we are")
    st.write(
        """
        급격한 고령화로 독거노인이 늘어나면서 외로움과 요양시설 입소 부담이 커지고, 
        동시에 청년층은 높은 주거비로 안정적 거주가 어려워졌습니다.
        이를 해결하기 위해 노인과 청년이 한 공간에서 상생하는 쉐어하우스 플랫폼을 추진하며, 
        초기에는 간단한 돌봄 서비스를 제공해 심리적 장벽을 낮추고자 합니다.
        """
    )

# 첫 번째 행 (이미지 3개)
row1_col1, row1_col2, row1_col3 = st.columns(3)

with row1_col1:
    st.image("image/신원확인.jpg", use_container_width=True)  # 이미지 경로 수정
with row1_col2:
    st.image("image/친절.png", use_container_width=True)
with row1_col3:
    st.image("image/돌봄.jpg", use_container_width=True)

# 두 번째 행 (설명 3개)
row2_col1, row2_col2, row2_col3 = st.columns(3)

with row2_col1:
    st.markdown("**철저한 신원 확인**")
with row2_col2:
    st.markdown("**친절한 매칭 서비스**")
with row2_col3:
    st.markdown("**원활한 돌봄 서비스**")

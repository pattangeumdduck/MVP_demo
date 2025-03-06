import streamlit as st
import re

# 세션 스테이트 초기화 (유저 정보 저장용)
if "users" not in st.session_state:
    st.session_state["users"] = {}
if "preferences" not in st.session_state:
    st.session_state["preferences"] = {}
if "user_type" not in st.session_state:
    st.session_state["user_type"] = None
if "survey_step" not in st.session_state:
    st.session_state["survey_step"] = 0
if "survey_answers" not in st.session_state:
    st.session_state["survey_answers"] = {}

# 설문조사 질문 리스트 (3개씩 그룹화하여 표시)
survey_questions = [
    [("이름:", "text"), ("나이:", "number"), ("성별:", "select", ["남성", "여성", "기타"])],
    [("평소 기상 및 취침 시간은?", "select", ["아침형", "밤형", "유동적"]),
     ("집에서 주로 보내는 시간:", "select", ["많음", "보통", "적음"]),
     ("하루 중 가장 활발한 시간대는 언제인가?", "text")],
    [("주중과 주말의 생활 패턴은 어떻게 다른가?", "text"),
     ("반려동물을 키우고 있거나 키울 계획이 있는가?", "radio", ["네", "아니요"]),
     ("흡연 여부 및 주류 섭취 빈도:", "text")],
    [("종교 또는 신념이 있는가?", "radio", ["네", "아니요"]),
     ("청결 및 정리정돈에 대한 기준이 높은가?", "radio", ["예", "아니요", "보통"]),
     ("조용한 환경과 시끌벅적한 환경 중 어느 것을 선호하는가?", "radio", ["조용한 환경", "시끌벅적한 환경"])],
    [("공동생활에서 가장 중요하게 생각하는 요소는?", "text")]
]

def show_survey_page():
    st.title("사전 설문조사")
    step = st.session_state["survey_step"]
    
    st.subheader(f"질문 {step + 1}/{len(survey_questions)}")
    
    for question_data in survey_questions[step]:
        question, q_type, *options = question_data
        
        if q_type == "text":
            answer = st.text_input(question, st.session_state["survey_answers"].get(question, ""))
        elif q_type == "number":
            answer = st.number_input(question, min_value=1, max_value=120, value=st.session_state["survey_answers"].get(question, 70))
        elif q_type == "select":
            answer = st.selectbox(question, options[0], index=options[0].index(st.session_state["survey_answers"].get(question, options[0][0])))
        elif q_type == "radio":
            answer = st.radio(question, options[0], index=options[0].index(st.session_state["survey_answers"].get(question, options[0][0])))
        
        st.session_state["survey_answers"][question] = answer
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("이전 질문") and step > 0:
            st.session_state["survey_step"] -= 1
    with col2:
        if st.button("다음 질문") and step < len(survey_questions) - 1:
            st.session_state["survey_step"] += 1
    
    if step == len(survey_questions) - 1:
        st.subheader("회원가입으로 이동")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("노인 회원가입으로 이동"):
                st.session_state["user_type"] = "노인"
                st.session_state["page"] = "signup"
        with col2:
            if st.button("청년 회원가입으로 이동"):
                st.session_state["user_type"] = "청년"
                st.session_state["page"] = "signup"

# 회원가입 화면 함수
def show_signup_page():
    st.title("회원가입 화면")
    user_type = st.session_state.get("user_type", "")
    st.write(f"현재 가입 대상: {user_type}")

    username = st.text_input("사용자 이름")
    password = st.text_input("비밀번호", type="password")
    preference = st.text_input("선호 사항")

    username_valid = bool(re.match(r"^[a-zA-Z0-9_]{5,20}$", username))
    password_valid = bool(re.match(r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$", password))

    if st.button(f"{user_type} 회원 가입하기"):
        if not username_valid:
            st.warning("아이디는 5~20자의 영문, 숫자, 밑줄(_)만 사용할 수 있습니다.")
        elif not password_valid:
            st.warning("비밀번호는 최소 8자 이상이며, 숫자와 문자를 포함해야 합니다.")
        elif username in st.session_state["users"]:
            st.warning("이미 존재하는 사용자 이름입니다. 다른 이름을 사용해주세요.")
        else:
            st.session_state["users"][username] = password
            st.session_state["preferences"][username] = preference
            st.success(f"{username}님 회원가입을 축하드립니다! ({user_type} 그룹)")

    if st.button("설문조사 다시 보기"):
        st.session_state["page"] = "survey"
        st.session_state["survey_step"] = 0

# 메인 함수
def main():
    if "page" not in st.session_state:
        st.session_state["page"] = "survey"
    if st.session_state["page"] == "survey":
        show_survey_page()
    else:
        show_signup_page()

if __name__ == "__main__":
    main()
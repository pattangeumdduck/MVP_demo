import streamlit as st

def main():
    st.title("매칭 화면")
    st.write("저장된 사용자 데이터를 바탕으로 간단히 매칭 기능을 시연합니다.")

    # 로그인/매칭 시나리오
    login_username = st.text_input("사용자 이름")
    login_password = st.text_input("비밀번호", type="password")

    if st.button("로그인"):
        if login_username not in st.session_state["users"]:
            st.error("존재하지 않는 사용자입니다.")
        else:
            real_password = st.session_state["users"][login_username]
            if real_password != login_password:
                st.error("비밀번호가 틀렸습니다.")
            else:
                st.success(f"{login_username}님 환영합니다!")

                # 매칭 로직 (단순히 동일한 preference를 가진 사람 찾기)
                user_pref = st.session_state["preferences"][login_username]
                matched_user = None
                for user, pref in st.session_state["preferences"].items():
                    if user != login_username and pref == user_pref:
                        matched_user = user
                        break

                if matched_user:
                    st.success(f"‘{matched_user}’ 님과 매칭되었습니다!")
                else:
                    st.info("조건에 맞는 매칭 상대가 없습니다.")

if __name__ == "__main__":
    main()

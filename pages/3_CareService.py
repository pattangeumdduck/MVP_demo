import streamlit as st

if "initialized" not in st.session_state:
    st.session_state["initialized"] = True
    st.session_state["elders_data"] = []
    st.session_state["page"] = 0

# ---------------------------------------------
# 0) Session State에 elders_data가 없으면 초기화
# ---------------------------------------------
if "elders_data" not in st.session_state:
    st.session_state["elders_data"] = [
        {
            "name": "김철수 할아버지",
            "desc": "혼자 계시지만 매우 활발하신 성격입니다.",
            "contact": "010-1234-5678",
            "image_url": "https://via.placeholder.com/200?text=Grandpa1"
        },
        {
            "name": "이영희 할머니",
            "desc": "요리와 가드닝을 좋아하세요.",
            "contact": "010-1111-2222",
            "image_url": "https://via.placeholder.com/200?text=Grandma1"
        }
    ]

# 한 페이지에 보여줄 아이템 수 (3행 × 3열 = 9)
ITEMS_PER_PAGE = 9

# 현재 페이지 인덱스 (0부터 시작)
if "page" not in st.session_state:
    st.session_state["page"] = 0

def main():
    st.title("돌봄 대상자 등록/삭제")
    
    # ---------------------------------------------
    # 1) 돌봄 대상자 등록 섹션
    # ---------------------------------------------
    st.subheader("돌봄 대상자 등록")
    with st.expander("새 대상자 입력 (클릭하여 펼치기)"):
        new_name = st.text_input("이름")
        new_desc = st.text_area("소개/특이사항")
        new_contact = st.text_input("연락처")
        new_image_url = st.text_input("이미지 URL (선택)",
                                      help="없으면 기본 placeholder 이미지를 사용합니다.")

        if st.button("등록하기"):
            if not new_name:
                st.warning("이름은 필수 항목입니다.")
            else:
                if not new_image_url:
                    new_image_url = "https://via.placeholder.com/200?text=No+Image"
                st.session_state["elders_data"].append({
                    "name": new_name,
                    "desc": new_desc,
                    "contact": new_contact,
                    "image_url": new_image_url
                })
                st.success(f"'{new_name}' 대상자가 등록되었습니다.")
                st.experimental_rerun()

    st.divider()

    # ---------------------------------------------
    # 2) 페이지네이션 & 그리드 표시
    # ---------------------------------------------
    total_items = len(st.session_state["elders_data"])
    total_pages = (total_items + ITEMS_PER_PAGE - 1) // ITEMS_PER_PAGE  # 올림

    start_idx = st.session_state["page"] * ITEMS_PER_PAGE
    end_idx = start_idx + ITEMS_PER_PAGE

    # 현재 페이지에 해당하는 데이터 슬라이싱
    elders_to_show = st.session_state["elders_data"][start_idx:end_idx]

    st.write(f"총 {total_items}명 중 현재 페이지: {st.session_state['page']+1} / {total_pages}")

    # ---------- 3×3 그리드로 표시 ----------
    ROWS = 3
    COLS = 3
    
    for row_index in range(ROWS):
        # 한 행당 3개의 column 생성
        cols = st.columns(COLS)
        for col_index in range(COLS):
            # elders_to_show에서 현재 표시할 아이템의 인덱스
            i = row_index * COLS + col_index
            if i >= len(elders_to_show):
                break

            # 실제 elders_data 내 인덱스 계산
            real_index = start_idx + i  
            elder = elders_to_show[i]

            with cols[col_index]:
                st.image(elder["image_url"], width=150)
                st.subheader(elder["name"])
                st.write(elder["desc"])
                st.caption(f"연락처: {elder['contact']}")

                # 삭제 버튼 추가
                if st.button(f"삭제 ({elder['name']})", key=f"delete_{real_index}"):
                    del st.session_state["elders_data"][real_index]
                    st.success(f"'{elder['name']}' 대상자가 삭제되었습니다.")
                    st.experimental_rerun()

    # ---------------------------------------------
    # 3) 페이지네이션 버튼
    # ---------------------------------------------
    col1, col2 = st.columns(2)
    with col1:
        if st.button("이전 페이지") and st.session_state["page"] > 0:
            st.session_state["page"] -= 1
            st.experimental_rerun()
    with col2:
        if st.button("다음 페이지") and st.session_state["page"] < total_pages - 1:
            st.session_state["page"] += 1
            st.experimental_rerun()

if __name__ == "__main__":
    main()

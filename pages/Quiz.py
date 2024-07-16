import streamlit as st

# 초기 상태 설정
if 'result1' not in st.session_state:
    st.session_state.result1 = 0  # 기본값 설정
if 'result2' not in st.session_state:
    st.session_state.result2 = 0  # 기본값 설정

st.write("정답을 입력 또는 체크해주세요")

# 첫 번째 질문
answer1 = ["python", "파이썬"]
quiz1 = st.text_input("Streamlit을 구성하는 언어는?")
if quiz1 in answer1:
    st.session_state.result1 = 50

# 두 번째 질문
genre = st.radio(
    "***1+1=?***",
    ["***1***", "***2***", "***3***", "***4***", "***5***"]
)

if genre == "***1***":
    st.session_state.result2 = 0
elif genre == "***2***":
    st.session_state.result2 = 50
elif genre in ["***3***", "***4***", "***5***"]:
    st.session_state.result2 = 0


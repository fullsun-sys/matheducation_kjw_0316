[import streamlit as st

st.title("Streamlit 요소 데모")

st.header("텍스트 요소")
st.text("이것은 일반 텍스트입니다.")
st.markdown("**마크다운** 지원합니다.")
st.code("print('Hello, Streamlit!')", language="python")
st.caption("캡션 예시")
st.subheader("서브헤더 예시")
st.write("st.write()는 다양한 타입을 출력합니다.")

st.header("입력 요소")
st.button("버튼")
st.checkbox("체크박스")
st.radio("라디오 버튼", ["옵션 1", "옵션 2", "옵션 3"])
st.selectbox("셀렉트박스", ["A", "B", "C"])
st.multiselect("멀티셀렉트", ["X", "Y", "Z"])
st.slider("슬라이더", 0, 100, 50)
st.text_input("텍스트 입력")
st.number_input("숫자 입력", min_value=0, max_value=10, value=5)
st.date_input("날짜 입력")
st.time_input("시간 입력")
st.file_uploader("파일 업로드")

st.header("데이터 표시 요소")
st.table({"A": [1,2], "B": [3,4]})
st.dataframe({"A": [1,2], "B": [3,4]})
st.json({"key": "value", "number": 123})

st.header("그래프 및 이미지")
import numpy as np
import matplotlib.pyplot as plt
arr = np.random.randn(100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)
st.pyplot(fig)

st.image("https://static.streamlit.io/examples/dog.jpg", caption="이미지 예시")

st.header("알림 및 진행바")
st.success("성공 메시지")
st.info("정보 메시지")
st.warning("경고 메시지")
st.error("에러 메시지")
st.progress(70)

st.header("기타 요소")
st.sidebar.title("사이드바 예시")
st.sidebar.button("사이드바 버튼")
st.sidebar.selectbox("사이드바 셀렉트박스", ["1", "2", "3"])

st.expander("확장 가능한 영역").write("여기에 내용을 넣을 수 있습니다.")

# ...existing code...
[import streamlit as st

st.title("Streamlit 요소 데모")

st.header("텍스트 요소")
st.text("이것은 일반 텍스트입니다.")
st.markdown("**마크다운** 지원합니다.")
st.code("print('Hello, Streamlit!')", language="python")
st.caption("캡션 예시")
st.subheader("서브헤더 예시")
st.write("st.write()는 다양한 타입을 출력합니다.")

st.header("입력 요소")
st.button("버튼")
st.checkbox("체크박스")
st.radio("라디오 버튼", ["옵션 1", "옵션 2", "옵션 3"])
st.selectbox("셀렉트박스", ["A", "B", "C"])
st.multiselect("멀티셀렉트", ["X", "Y", "Z"])
st.slider("슬라이더", 0, 100, 50)
st.text_input("텍스트 입력")
st.number_input("숫자 입력", min_value=0, max_value=10, value=5)
st.date_input("날짜 입력")
st.time_input("시간 입력")
st.file_uploader("파일 업로드")

st.header("데이터 표시 요소")
st.table({"A": [1,2], "B": [3,4]})
st.dataframe({"A": [1,2], "B": [3,4]})
st.json({"key": "value", "number": 123})

st.header("그래프 및 이미지")
import numpy as np
import matplotlib.pyplot as plt
arr = np.random.randn(100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)
st.pyplot(fig)

st.image("https://static.streamlit.io/examples/dog.jpg", caption="이미지 예시")

st.header("알림 및 진행바")
st.success("성공 메시지")
st.info("정보 메시지")
st.warning("경고 메시지")
st.error("에러 메시지")
st.progress(70)

st.header("기타 요소")
st.sidebar.title("사이드바 예시")
st.sidebar.button("사이드바 버튼")
st.sidebar.selectbox("사이드바 셀렉트박스", ["1", "2", "3"])

st.expander("확장 가능한 영역").write("여기에 내용을 넣을 수 있습니다.")

# ...existing code...

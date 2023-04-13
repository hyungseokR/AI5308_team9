import streamlit as st

# 페이지 기본 설정
st.set_page_config(
    page_icon="🐶",
    page_title="류형석",
    layout="wide",
)

st.subheader("Documents")

if st.button("app.py 코드 보기"):
    code = '''
    import streamlit as st
    import pandas as pd
    import numpy as np

    from time import sleep

    # 페이지 기본 설정
    st.set_page_config(
        page_icon="🐱‍🏍",
        page_title="류형석",
        layout="wide",
    )

    # 로딩바 구현하기
    with st.spinner(text="페이지 로딩중..."):
        sleep(2)

    # 페이지 헤더, 서브헤더 제목 설정
    st.header("환영합니다👋")
    st.subheader("안녕하세요.")

    # 페이지 컬럼 분할(예: 부트스트랩 컬럼, 그리드)
    cols = st.columns((1, 1, 2))
    cols[0].metric("10/11", "15 °C", "2")
    cols[0].metric("10/12", "17 °C", "2 °F")
    cols[0].metric("10/13", "15 °C", "2")
    cols[1].metric("10/14", "17 °C", "2 °F")
    cols[1].metric("10/15", "14 °C", "-3 °F")
    cols[1].metric("10/16", "13 °C", "-1 °F")

    # 라인 그래프 데이터 생성(with. Pandas)
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c'])

    # 컬럼 나머지 부분에 라인차트 생성
    cols[2].line_chart(chart_data)
    '''
    st.code(code, language='python')
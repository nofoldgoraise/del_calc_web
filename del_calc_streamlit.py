import streamlit as st

# st.markdown(""" # 폰트 css
# <style>
# html, body, [class*="css"] {
#     font-size: 20px;
# }
# </style>
# """, unsafe_allow_html=True)

st.title("배달 일당 계산기") # 페이지 제목

if "reset" not in st.session_state:
  st.session_state.reset = False

if st.session_state.reset:
  st.session_state.work_time = 0
  st.session_state.rest_time = 0
  st.session_state.oil_price = 0
  st.session_state.food_price = 0
  st.session_state.total_cash = 0
  st.session_state.delivery_count = 0
  st.session_state.reset = False # 초기화 후 reset을 다시 False 로 설정 (리셋이 유지되지않도록)

# Label, Entry 생성 (입력창)
work_time = st.number_input("총 운행시간(시간)", step=1, key = "work_time")
rest_time = st.number_input("총 휴식시간(시간)", step=1, key = "rest_time")
oil_price = st.number_input("기름값", step=1, key = "oil_price")
food_price = st.number_input("식비", step=1, key = "food_price")
total_cash = st.number_input("매출", step=1, key = "total_cash")
delivery_count = st.number_input("건 수", step=1, key = "delivery_count")

# Button 생성 및 설정 (계산)
if st.button("계 산"):
  try:
    real_total_time = work_time - rest_time # 실 운행시간
    today_pay = oil_price + food_price # 총 지출
    avr_count = f"{delivery_count / real_total_time:.1f}" # 시간당 건수
    avr_price = total_cash // delivery_count # 건 당 평균 단가
    get_money = total_cash - today_pay # 순수익
    avr_money = total_cash // real_total_time # 시간당 급여 (시급)

    result_text = f"""실 운행시간: {real_total_time}시간
  지출: {today_pay:,}원
  건 수: {delivery_count}건
  매 출: {total_cash:,}원
  시간당 건 수: {avr_count}건
  평균 단가: {avr_price:,}원
  시 급: {avr_money:,}원
  ★순 수익: {get_money:,}원"""
    st.write(f"실 운행시간: {real_total_time}시간")
    st.write(f"지출: {today_pay:,}원")
    st.write(f"건 수: {delivery_count}건")
    st.write(f"매 출: {total_cash:,}원")
    st.write(f"시간당 건 수: {avr_count}건")
    st.write(f"평균 단가: {avr_price:,}원")
    st.write(f"★시 급: {avr_money:,}원")
    st.write(f"★순 수익: {get_money:,}원")
  except ZeroDivisionError:
    st.write("[오류] 잘못입력하셨습니다. 다시 입력해주세요.")
    
# Button 생성 및 설정 (초기화)
if st.button("초기화"):
  st.session_state.reset = True # reset = True 설정
  st.rerun() # 스크립트 다시시작

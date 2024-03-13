import streamlit as st 
import time
from datetime import datetime

st.header("daily lift")
st.write("Note Path")
#while true: ทำลูป
name = st.text_input("ชื่อ/เรื่อง")

day = st.text_input("วันที่เท่าไหร่")

what = st.text_input("ทำอะไร")

timer = st.number_input("เวลาเมื่อไหร่",step=1.0)
# if timer < datetime.now().strftime:
st.write(f"ชื่อ: {name}")
st.write(f"วันที่: {day}")
st.write(f"เวลาที่: {timer}")
st.write(f"ทำอะไรบ้าง: {what}")
timee = st.empty()
while True:
    current_time = datetime.now().strftime("%H:%M:%S")
    timee.text(f"เวลาปัจจุบัน: {current_time}")
    time.sleep(1)
# ยังไม่เสร็จ
 

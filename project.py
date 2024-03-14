import streamlit as st 
import datetime
import time
st.header("Daily/NotePath")

select = st.radio("select",('Daily', 'NotePath'))
if select == 'Daily': 
 st.write('You selected Daily.')
 name = st.text_input("ชื่อ/เรื่อง")
 dayold = st.number_input("กรุณาใส่ วันที่", step=0)
 timer = st.number_input("เวลาเมื่อไหร่", step=0)
 whatt = st.text_input("กรุณาใส่ รายละเอียด")
 
 st.write(f"ชื่อ: {name}")
 st.write(f"วันที่: {dayold}")
 st.write(f"เวลาที่: {timer}")
 st.write(f"ทำอะไรบ้าง: {whatt}")

elif select == 'NotePath':
 st.write('You selected NotePath.')
 daynow = st.number_input("วันนี้", step=0)
 namenxt = st.text_input("ชื่อ/เรื่อง")
 daynext = st.number_input("กรุณากำหนดวันที่ต้องการ", step=0)
 timer = st.number_input("กรุณากำหนดเวลาต้องการ", step=0.0)
 what = st.text_input("กรุณาใส่รายละเอียด")
 
 st.write(f"ชื่อ: {namenxt}")
 st.write(f"วันที่: {daynext}")
 st.write(f"เวลาที่: {timer}")
 st.write(f"ทำอะไรบ้าง: {what}")
 
 totaltime = datetime.datetime.now()
 label = st.empty()
 showtime = totaltime.hour * 3600 + totaltime.minute * 60 + totaltime.second  + (daynext-daynow)*24*3600 +(timer//1)*3600 + (timer//1-timer)*60
 while showtime > 0:
    label.write(f"เวลาที่เหลือ: {showtime} วินาที")
    showtime -= 1
    time.sleep(1)
 st.write("ครบกำหนดเวลาแล้ว")
#  
# on 19 APRIL 2024

import streamlit as st
import pandas as pd

st.title("AI ELITE STREAMLIT DEMO")

st.header("Session for ELITE-18")

st.subheader("By Lakshmi Teja")

username = st.text_input("please enter your name:")

st.write(f"Hello, {username}! welcome to the session")

course = st.radio("Select your course",["Data Analysis", "Data Science", "Full Stack"])

st.write(f"You have opted for {course}")

no_of_months = st.number_input("How many months would you like to dedicate for completing the course?")

st.write(f"You have opted for {course}. You decided to complete the course in {no_of_months} months time period.")

Ratings = st.slider(f"Choose your ratings for the {course}",min_value=1.0,max_value=5.0,step=0.5)

st.write(f"You have given {Ratings} rating to the {course} course")

if course == "Data Analysis":
    st.write("You have 4 months to complete the course")
elif course == "Data Science":
    st.write("You have 9 months to complete the course")

st.image(r"https://img-s-msn-com.akamaized.net/tenant/amp/entityid/AA11N9kp.img")

st.video(r"https://www.youtube.com/watch?v=xnubQ829q0c")

st.audio(r"https://music.youtube.com/watch?v=Xg0AvNZkERM&si=n_XaupF9ucqc6wVI")

# for page actions
# st.snow()
# st.balloons()

st.sidebar.title("select a page")

# charts in streamlit 
# examples below
# st.area_chart
# st.bar_chart

st.line_chart(data=[1,2,3,4,43,2,3,42,3])

# df = pd.DataFrame({"1":24,"2":52,"3":26,"4":64},columns=["Numbers","count"])
df = pd.DataFrame({"Numbers":[1,2,3,4]
                   ,"count":[25,6,42,53]})
st.write(df)

# st.checkbox()
st.code("a = input('Enter a name')")

# st.latex(r"$\mu$  $_1$ $\mu$  $_2$ ... $\mu$  $_{n-2}$ $\mu$ $_n$ ")

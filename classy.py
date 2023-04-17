import streamlit as st
from database import add_data
from database import add_attendance


def create_class():
   
    col1, col2 = st.columns(2)
   
    with col1:
   
        Dates = st.text_input("Date:")
   
        Subject = st.selectbox("Subject", ["Mathematics", "Science"],key='Subject')
   
        Teach_ID = st.text_input("Teacher ID :")


   
    with col2:
   
        Student_ID = st.text_input("Class rep ID :")
        class_ID = st.text_input("class ID :")
   
    if st.button("Add Subject"):
   
        add_data(Student_ID, Subject, Dates, Teach_ID,class_ID)
   
        st.success("Successfully added new class: {}".format(Subject))



            
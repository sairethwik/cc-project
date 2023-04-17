import streamlit as st
from database import add_data
from database import add_attendance

def attendance():


    Student_ID = st.text_input("student")

    Class_ID = st.text_input("Enter class_ID")
    
    Dates = st.text_input("Date")


    if st.button("Mark attendance"):

        add_attendance(Class_ID,Dates, Student_ID)

        st.success("Successfully updated attendance: {}".format(Student_ID))



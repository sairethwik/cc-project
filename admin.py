import streamlit as st
from database import add_student,remove_student


def manag():
    col1, col2 = st.columns(2)
    with col1:
        Student_ID =st.text_input("Student ID :")
        F_name = st.text_input("Add first name :")
        L_name = st.text_input("Add last name :")
    
    with col2:
        email_ID = st.text_input("Email ID :")
        Phone_no = st.text_input("Phone_no :")
        password = st.text_input("enter password :")

    if st.button("Add Student"):
        add_student(Student_ID,F_name,L_name,email_ID,Phone_no,password)
        st.success("Successfully added new Student: {}".format(Student_ID))
    #ERROR
    if st.button("Remove Student"):
        remove_student(Student_ID)
        st.success("Student has been removed")

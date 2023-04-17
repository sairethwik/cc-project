import streamlit as st
from database import *

def studentt_update():

    Student_ID = st.text_input("student ID")
    # F_name =st.text_input("Enter real first name")
    # L_name =st.text_input("Enter real last name")
    # email_ID=st.text_input("Enter real email_ID")
    # Phone_no=st.text_input("Enter real Phone no")
    # password=st.text_input("Enter real Password")

    new_Student_ID = st.text_input("new student ID")
    new_F_name =st.text_input("Enter First name")
    new_L_name =st.text_input("Enter last name")
    new_email_ID=st.text_input("Enter email_ID")
    new_phone_no=st.text_input("Enter Phone no")
    new_password=st.text_input("Enter Password")
    


    if st.button("Update details"):

        update_details(new_Student_ID,new_F_name,new_L_name,new_email_ID,new_phone_no,new_password,Student_ID)

        st.success("Successfully updated details: {}")


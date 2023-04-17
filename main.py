import streamlit as st
import mysql.connector


from delete import delete
from read import read
from update import update
from classy import create_class
from admin import manag
from attendance import *
from student_update import *
from view_attendance import *
from database import *


#hi rethwik
def main():
  
    st.title("PES2UG20CS394 Student attendance management system :")
  
    menu = ["Teacher", "Admin", "Student", "View attendance","Mark Attendance","Update"]
    create_table()

    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Teacher":
  
        st.subheader("Enter the class details:")
  
        create_class()



    elif choice == "View attendance":

        st.subheader("View Attendances")
        view_attend()
        
        


    elif choice == "Student":

        st.subheader("View classes to attend")

        update()



    elif choice == "Remove":

        st.subheader("Delete created tasks")
        delete()



    elif choice == "Admin":

        st.subheader("Add teacher/student details:")

        manag()
    elif choice =="Mark Attendance":

        st.subheader("Add attendance details")
        attendance()
    elif choice =="Update":

        st.subheader("Update student details here :")
        studentt_update()

    else:

        st.subheader("About tasks")

if __name__ == '__main__':
    main()




import datetime

import pandas as pd
import streamlit as st
from database import view_all_data, view_only_class_names, get_Train, update_details


def update():
    result = view_all_data('Student_ID','Subject','Dates','Teach_ID','class_ID')

    # st.write(result)

    df = pd.DataFrame(result, columns=['Student_ID','Subject','Dates','Teach_ID','class_ID'])

    with st.expander("Current Classes to attend"):

        st.dataframe(df)

    list_of_classes = [i[0] for i in view_only_class_names()]
'''
    selected_train = st.selectbox("Class to edit", list_of_classes)

    selected_result = get_Train(selected_train)

    # st.write(selected_result)

    if selected_result:

        Student_ID = selected_result[0][0]

        Subject = selected_result[0][1]

        Dates = selected_result[0][2]

        Teach_ID = selected_result[0][3]



        # Layout of Create



        col1, col2 = st.columns(2)

        with col1:

            new_Student_ID = st.text_input("Student_ID:", new_Student_ID)

            new_Subject = st.text_input("Subject:", new_Subject)

        with col2:



            new_Dates = st.text_input("Date :", new_Dates)

            new_Teach_ID = st.text_input("new_Teach_ID",new_Teach_ID)

        if st.button("Update Train"):

            update_details(new_Train_no,new_Name,new_Train_type,new_source,new_Destination,new_Availability,Train_no,Name,Train_type,source,Destination,Availability)

            st.success("Successfully updated:: {} to ::{}".format(Name, new_Name))



    result2 = view_all_data('Student_ID','Subject','Dates','Teach_ID')

    df2 = pd.DataFrame(result2, columns=['Student_ID','Subject','Dates','Teach_ID'])

    with st.expander("Updated data"):

        st.dataframe(df2)

'''

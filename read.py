import pandas as pd

import streamlit as st

import plotly.express as px

from database import view_all_data





def read():

    result = view_all_data('Student_ID','Subject','Dates','Teach_ID','class_ID')

    # st.write(result)
    df = pd.DataFrame(result, columns=['Student_ID','Subject','Dates','Teach_ID','class_ID'])

    with st.expander("View all Classes"):

        st.dataframe(df)


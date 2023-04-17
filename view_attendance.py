import pandas as pd

import streamlit as st

import plotly.express as px

from database import *


def view_attend():

    result = view_attendan('Class_ID','Dates','Student_ID')

    # st.write(result)
    df = pd.DataFrame(result, columns=['Class_ID','Dates','Student_ID'])

    with st.expander("View attendance"):

        st.dataframe(df)
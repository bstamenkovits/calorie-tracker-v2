import streamlit as st
import pandas as pd
from interface import DatabaseInterface

db_interface = DatabaseInterface()

st.set_page_config(
    page_title="Food Overview",
    page_icon="🥦",
)

st.write("# Food Overview 🥦")
st.write("View and Log Food and Calorie Intake")

users = db_interface.get_users()

user = st.pills("User", options=[u.name for u in users], selection_mode="single")
date = st.date_input("Date", value=pd.to_datetime("today"))
date = date.strftime("%Y-%m-%d")



import streamlit as st
import pandas as pd
from interface import DatabaseInterface
from models.udf.logs_food_input import LogsFoodInputData
from datetime import datetime

db_interface = DatabaseInterface()

st.set_page_config(
    page_title="Food Overview",
    page_icon="🥦",
    layout="wide",
)

st.write("# Food Overview 🥦")
st.write("View and Log Food and Calorie Intake")

users = db_interface.get_users()
meals = db_interface.get_meals()


available_ingredients = db_interface.get_ingredients()

user = st.pills("User", options=users, format_func=lambda u: u.name, selection_mode="single")
date = st.date_input("Date", value=pd.to_datetime("today"))
date = datetime(3000, 1, 1)
# date = date.strftime("%Y-%m-%d")

if user is None:
    st.warning("Please select a user.")
    st.stop()
logs_food = db_interface.get_logs_food(LogsFoodInputData(user_id=user.id, date_added=date))

col_ingredients, col_quantity, col_weight, col_calories = st.columns(4)
with col_ingredients:
    # st.write("**Ingredient**")
    for log in logs_food:
        # st.write(f"{log.ingredient_name}")
        idx = available_ingredients.index(next(i for i in available_ingredients if i.name == log.ingredient_name))
        st.selectbox("Select Ingredient", options=available_ingredients, format_func=lambda i: i.name, index=idx, label_visibility="collapsed")
with col_quantity:
    for log in logs_food:
        st.number_input("Quantity", min_value=0.0, value=log.quantity, step=0.1, label_visibility="collapsed")
        st.write(f"{log.serving_name}")
with col_weight:
    for log in logs_food:
        st.write(f"{log.total_weight_g} g")
with col_calories:
    for log in logs_food:
        st.write(f"{log.total_calories_kcal} kcal")

# df_logs_food = pd.DataFrame([data.model_dump() for data in logs_food])
# st.dataframe(df_logs_food)

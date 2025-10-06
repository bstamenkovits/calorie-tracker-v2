from supabase import create_client, Client
import streamlit as st
import pandas as pd
import hashlib

"""
Quick and dirty script to upload existing ingredients database (csv file) to Supabase.
"""


supabase_url = st.secrets["SUPABASE"]["url"]
supabase_key = st.secrets["SUPABASE"]["api_key"]
supabase: Client = create_client(supabase_url, supabase_key)


column_map = {
    "Name": "name",
    "Fat (g)": "fat_g",
    "Carbs (g)": "carbs_g",
    "Protein (g)": "protein_g",
    "Calories (kcal)": "calories_kcal",
    "Type": "type",
    "Serving Name": "serving_name",
    "Single Serving (g)": "serving_size_g",
}

def generate_ingredient_technical_key(row):
    concat_values = f"{row['name']}{row['calories_kcal']}{row['fat_g']}{row['carbs_g']}{row['protein_g']}{row['type']}"
    return hashlib.md5(concat_values.encode('utf-8')).hexdigest()


def generate_serving_technical_key(row):
    concat_values = f"{row['name']}{row['serving_name']}{row['serving_size_g']}"
    return hashlib.md5(concat_values.encode('utf-8')).hexdigest()


ingredients = pd.read_csv("./util/ingredients.csv")
ingredients = ingredients.rename(columns=column_map)
ingredients["ingredient_id"] = ingredients.apply(generate_ingredient_technical_key, axis=1)
ingredients["serving_id"] = ingredients.apply(generate_serving_technical_key, axis=1)


def upload_ingredients(ingredients=ingredients):
    ingredients = ingredients.rename(columns={"ingredient_id": "id"})
    ingredients = ingredients[["id", "name", "calories_kcal", "fat_g", "carbs_g", "protein_g", "type", "serving_id", "serving_name", "serving_size_g"]]
    ingredients = ingredients.to_dict(orient="records")

    response = (
        supabase.table("ingredients")
        .insert(ingredients)
        .execute()
    )


def upload_servings(ingredients=ingredients):
    ingredients = ingredients.rename(columns={"serving_id": "id", "serving_name": "name", "serving_size_g": "size_g"})
    ingredients = ingredients[["id", "ingredient_id", "name", "size_g"]]
    ingredients = ingredients.to_dict(orient="records")

    response = (
        supabase.table("servings")
        .insert(ingredients)
        .execute()
    )

if __name__ == "__main__":
    # upload_ingredients()
    upload_servings()

import streamlit as st
from supabase import Client, create_client
import pandas as pd

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

supabase_url = st.secrets["SUPABASE"]["url"]
supabase_key = st.secrets["SUPABASE"]["api_key"]
supabase: Client = create_client(supabase_url, supabase_key)

response = supabase.table("ingredients").select("*").execute()
df = pd.DataFrame(response.data)
st.dataframe(df)

from pydantic import BaseModel, computed_field
from util.hash import generate_technical_key
import streamlit as st

class UserData(BaseModel):
    name: str

    @computed_field
    def id(self) -> str:
        return generate_technical_key(self.name)


if __name__ == "__main__":
    from interface.supabase_interface import SupabaseInterface
    from util.hash import generate_technical_key
    interface = SupabaseInterface()

    user1 = UserData(
        id=generate_technical_key(st.secrets["USERS"]["user1"]),
        name=st.secrets["USERS"]["user1"]
    )

    user2 = UserData(
        id=generate_technical_key(st.secrets["USERS"]["user2"]),
        name=st.secrets["USERS"]["user2"]
    )

    response = interface.insert_user(user1)
    response = interface.insert_user(user2)

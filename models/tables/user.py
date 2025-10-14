from pydantic import BaseModel, Field
from util.hash import generate_technical_key
from typing import Optional
import streamlit as st

class UserData(BaseModel):
    id: Optional[str] = Field(default=None)
    name: str

    def model_post_init(self, __context):
        """Called after model initialization to set computed fields"""
        if self.id is None:
            self.id = generate_technical_key(self.name)


if __name__ == "__main__":
    # from interface.supabase_interface import SupabaseInterface
    # interface = SupabaseInterface()
    from interface import DatabaseInterface
    interface = DatabaseInterface()

    # user1 = UserData(name=st.secrets["USERS"]["user1"])
    # user2 = UserData(name=st.secrets["USERS"]["user2"])

    # response = interface.insert_user(user1)
    # response = interface.insert_user(user2)

    test_user = UserData(name="__test_user__")
    response = interface.insert_user(test_user)

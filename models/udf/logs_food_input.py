import datetime
from pydantic import BaseModel, Field
from util.hash import generate_technical_key
from typing import Optional


class LogsFoodInputData(BaseModel):
    user_id: Optional[str] = Field(default=None)
    date_added: datetime.datetime = Field(default_factory=datetime.datetime.now)

    def to_dict(self):
        """Convert to dictionary with datetime as ISO string for Supabase"""
        data = self.model_dump()
        # Convert datetime to ISO format string
        data['date_added'] = self.date_added.isoformat()
        return data

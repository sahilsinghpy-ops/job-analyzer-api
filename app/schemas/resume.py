from pydantic import BaseModel
from datetime import datetime

class ResumeBase(BaseModel):
    title: str
    raw_text: str
    skills: list[str]

class ResumeCreate(ResumeBase):
    pass # It just inherits everything from ResumeBase

class ResumeResponse(ResumeBase):
    id: int
    user_id: int
    created_at: datetime

    class Config:
        from_attributes = True
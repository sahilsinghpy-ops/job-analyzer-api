from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import JSONB
from app.db.database import Base

class JobDescription(Base):
    __tablename__ = "job_descriptions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    company_name = Column(String, nullable=False)
    role_title = Column(String, nullable=False)
    raw_text = Column(Text, nullable=False)
    required_skills = Column(JSONB, nullable=False, default=list) # e.g., ["AWS", "SQL"]
    created_at = Column(DateTime(timezone=True), server_default=func.now())
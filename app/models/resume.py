from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import JSONB
from app.db.database import Base

class Resume(Base):
    __tablename__ = "resumes" # Added 's'
    
    id = Column(Integer, primary_key=True, index=True)
    # Must match "users.id" exactly, and use lowercase "cascade"
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False) 
    title = Column(String, nullable=False)
    raw_text = Column(Text, nullable=False)
    skills = Column(JSONB, nullable=False, default=list)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
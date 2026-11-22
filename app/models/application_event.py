from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text
from sqlalchemy.sql import func
from app.db.database import Base

class ApplicationEvent(Base):
    __tablename__ = "application_events"

    id = Column(Integer, primary_key=True, index=True)
    application_id = Column(Integer, ForeignKey("applications.id", ondelete="CASCADE"), nullable=False)
    
    old_status = Column(String, nullable=True) # Can be null if it's the first event
    new_status = Column(String, nullable=False)
    note = Column(Text, nullable=True) # e.g., "Got a call from HR"
    created_at = Column(DateTime(timezone=True), server_default=func.now())
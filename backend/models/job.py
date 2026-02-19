from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from db.database import Base
from sqlalchemy import func

class storyJob(Base):
    __tablename__ = "story_jobs"

    id = Column(Integer, primary_key=True, index=True) ##primary key to uniquely identify each job and index for faster querying
    job_id = Column(String, index=True, unique=True)
    theme= Column(String) ##theme of the story to be generated
    story_id = Column(Integer, nullable=True) 
    session_id = Column(String, index=True) ##session id to link the job to a specific user session (index for faster querying)
    status = Column(String, index=True) ##status of the job (e.g., pending, in_progress, completed) (index for faster querying)
    error= Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now()) ##timestamp to track when the job was created
    completed_at = Column(DateTime(timezone=True), nullable=True) 
    
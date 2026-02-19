from pydantic import BaseModel
from typing import List, Optional, Dict
from datetime import datetime

class StoryJobBase(BaseModel):
    theme: str

class StoryJobresponse(StoryJobBase):
    job_id: str
    status: str
    created_at: datetime
    story_id: Optional[int] = None
    completed_at: Optional[datetime] = None
    error: Optional[str] = None

    class Config:
        from_attributes = True
        
class StoryJobCreate(StoryJobBase):
    pass
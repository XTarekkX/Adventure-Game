from pydantic import BaseModel
from typing import List, Optional, Dict
from datetime import datetime

class StoryOptionSchema(BaseModel):
    text: str
    node_id: Optional[int] = None

class StoryNodeBase(BaseModel):
    content: str
    is_ending: bool = False
    is_winning_ending: bool = False

class CompleteStoryNodeResponse(StoryNodeBase):
    id: int
    options: List[StoryOptionSchema]=[]

    class Config:
        from_attributes = True

class StoryBase(BaseModel):
    title: Optional[str] = None
    session_id: Optional[str] = None

    class Config:
        from_attributes = True

class CreateStoryRequest(StoryBase):
    theme: str

class CompleteStoryResponse(StoryBase):
    id: int
    created_at: datetime
    all_nodes: Dict[int, CompleteStoryNodeResponse]
    root_node: List[CompleteStoryNodeResponse]

    class Config:
        from_attributes = True
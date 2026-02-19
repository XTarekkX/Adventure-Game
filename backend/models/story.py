from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, JSON
from sqlalchemy.orm import relationship
from sqlalchemy import func 
from db.database import Base

class Story(Base):
    __tablename__ = "stories"

    id = Column(Integer, primary_key=True, index=True) ##primary key to uniquely identify each story and index for faster querying
    title = Column(String(255), index=True)
    content = Column(Text, index=True)
    session_id = Column(String(255), index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    nodes = relationship("StoryNode", back_populates="story") ##relationship to the Node model (one to many relationship) (a story can have multiple nodes) (back_populates to define the relationship in both models)

class StoryNode(Base):
    __tablename__ = "story_nodes"

    id = Column(Integer, primary_key=True, index=True)
    story_id = Column(Integer, ForeignKey("stories.id")) ##foreign key to link the node to the story (many to one relationship) (a node belongs to one story)
    content = Column(String, index=True)
    is_root = Column(Integer, default=False) ##flag to indicate if the node is the root node of the story (1 for root node, 0 for non-root node)
    is_end = Column(Integer, default=False) ##flag to indicate if the node is the end node of the story (1 for end node, 0 for non-end node)
    is_win = Column(Integer, default=False) ##flag to indicate if the node is a winning node of the story (1 for winning node, 0 for non-winning node)
    options= Column(JSON, default=list) ##options for the node (list of options for the user to choose from) (stored as JSON in the database)
    story = relationship("Story", back_populates="nodes") ##relationship to the Story model (many to one relationship) (back_populates to define the relationship in both models)
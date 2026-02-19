from typing import List, Optional, Dict, Any
from fastapi import APIRouter, Depends, HTTPException, Cookie, Response, BackgroundTasks
from db.database import get_db, SessionLocal
from sqlalchemy.orm import Session
from models.job import storyJob
from schemas.job import StoryJobresponse

router= APIRouter(##jobs specific route
    prefix="/jobs",
    tags=["jobs"]
)

@router.get("/{job_id}", response_model=StoryJobresponse)
def get_job_status(job_id: str, db: Session = Depends(get_db)):
    job= db.query(storyJob).filter(storyJob.job_id == job_id).first()
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    return job
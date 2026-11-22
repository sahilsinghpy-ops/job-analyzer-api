from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.db.database import get_db
from app.models.user import User
from app.models.resume import Resume
from app.schemas.resume import ResumeCreate, ResumeResponse
from app.api.deps import get_current_user

router = APIRouter(prefix="/resumes", tags=["Resumes"])

# 1. CREATE a resume
@router.post("/", response_model=ResumeResponse, status_code=status.HTTP_201_CREATED)
def create_resume(
    resume_in: ResumeCreate, 
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user) # <--- The Guard!
):
    # We link the resume to the logged-in user automatically
    new_resume = Resume(
        user_id=current_user.id,
        title=resume_in.title,
        raw_text=resume_in.raw_text,
        skills=resume_in.skills
    )
    db.add(new_resume)
    db.commit()
    db.refresh(new_resume)
    return new_resume

# 2. READ all your resumes
@router.get("/", response_model=List[ResumeResponse])
def get_resumes(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # Notice the filter: Only get resumes where the user_id matches the logged-in user
    resumes = db.query(Resume).filter(Resume.user_id == current_user.id).all()
    return resumes

# 3. DELETE a resume
@router.delete("/{resume_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_resume(
    resume_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # Find the resume
    resume = db.query(Resume).filter(Resume.id == resume_id).first()
    
    # Check if it exists
    if not resume:
        raise HTTPException(status_code=404, detail="Resume not found")
        
    # Check if the user actually owns this resume
    if resume.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to delete this resume")
        
    db.delete(resume)
    db.commit()
    return None
from fastapi import FastAPI
from app.api import auth, resume # <--- Add resumes here

app = FastAPI(title="Job Application Material Analyzer API")

app.include_router(auth.router)
app.include_router(resume.router) # <--- Add this line

@app.get("/health")
def health_check():
    return {"status": "ok"}
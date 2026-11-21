from fastapi import FastAPI
from app.api import auth

app = FastAPI(title="Job Application Material Analyzer API")

# This line is what connects the auth endpoints to the app
app.include_router(auth.router)

@app.get("/health")
def health_check():
    return {"status": "ok"}
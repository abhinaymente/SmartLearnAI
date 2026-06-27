from fastapi import FastAPI, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.core.database import get_db

app = FastAPI(
    title="SmartLearn AI API",
    description="AI-Powered Smart Learning Platform Backend",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to SmartLearn AI API",
        "status": "Backend is running successfully"
    }


@app.get("/db-test")
def test_database(db: Session = Depends(get_db)):
    result = db.execute(text("SELECT DATABASE();"))
    database_name = result.scalar()

    return {
        "status": "Connected Successfully",
        "database": database_name
    }
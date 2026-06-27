from fastapi import FastAPI

from app.core.database import Base, engine
from app.routes.auth import router as auth_router
from app.routes.users import router as users_router
from app.routes.pdf import router as pdf_router

from app.models.user import User
from app.models.pdf import PDF

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="SmartLearn AI API",
    version="1.0.0"
)

app.include_router(auth_router)
app.include_router(users_router)
app.include_router(pdf_router)
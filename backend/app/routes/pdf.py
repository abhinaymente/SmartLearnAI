from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.dependencies import get_current_user

from app.models.user import User

from app.schemas.pdf_schema import PDFResponse
from app.services.pdf_service import upload_pdf

router = APIRouter(
    prefix="/pdf",
    tags=["PDF"]
)


@router.post(
    "/upload",
    response_model=PDFResponse
)
def upload(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return upload_pdf(
        db,
        file,
        current_user
    )
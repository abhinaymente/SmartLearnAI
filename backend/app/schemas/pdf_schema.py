from pydantic import BaseModel
from datetime import datetime


class PDFResponse(BaseModel):
    id: int
    file_name: str
    original_filename: str
    file_path: str
    uploaded_at: datetime
    user_id: int
    extracted_text: str | None = None

    class Config:
        from_attributes = True
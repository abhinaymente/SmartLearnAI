import os
import shutil
import uuid

from sqlalchemy.orm import Session

from app.models.pdf import PDF


def upload_pdf(
    db: Session,
    file,
    current_user
):
    # Create uploads folder if it doesn't exist
    os.makedirs("uploads", exist_ok=True)

    # Save path
    unique_filename = f"{uuid.uuid4()}_{file.filename}"

    file_path = os.path.join(
        "uploads",
        unique_filename
    )

    # Save PDF to disk
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Create database object
    pdf = PDF(
    file_name=unique_filename,
    original_filename=file.filename,
    file_path=file_path,
    user_id=current_user.id
    )

    # Save in database
    db.add(pdf)
    db.commit()
    db.refresh(pdf)

    return pdf
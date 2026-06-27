from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user_schema import UserCreate
from app.core.security import hash_password


def create_user(db: Session, user_data: UserCreate):

    # Check if email already exists
    existing_user = db.query(User).filter(
        User.email == user_data.email
    ).first()

    if existing_user:
        raise ValueError("Email already registered")

    # Hash password
    hashed_password = hash_password(user_data.password)

    # Create User object
    new_user = User(
        full_name=user_data.full_name,
        email=user_data.email,
        password=hashed_password
    )

    # Save to database
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user
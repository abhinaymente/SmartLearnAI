from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user_schema import UserCreate,UserLogin
from app.core.security import hash_password, verify_password, create_access_token


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

def login_user(
    db: Session,
    email: str,
    password: str):

    # Find user by email
    existing_user = db.query(User).filter(
        User.email == email
    ).first()

    # User not found
    if not existing_user:
        raise ValueError("Invalid email or password")

    # Verify password
    if not verify_password(
        password,
        existing_user.password
    ):
        raise ValueError("Invalid email or password")

    # Generate JWT
    token = create_access_token(
        {
            "sub": existing_user.email
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }
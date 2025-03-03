# backend/app/services/user_service.py
from app.db.database import get_db
from app.db.models import User
from app.core.security import get_password_hash, verify_password
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

async def get_user_by_username(username: str, db: Session = next(get_db())):
    """
    Retrieve a user record by username.
    """
    return db.query(User).filter(User.username == username).first()

async def create_user(username: str, password: str, db: Session = next(get_db())):
    """
    Create a new user with a hashed password.
    """
    hashed_password = get_password_hash(password)
    user = User(username=username, hashed_password=hashed_password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

async def authenticate_user(username: str, password: str, db: Session = next(get_db())):
    """
    Authenticate the user by comparing the provided credentials with stored data.
    """
    user = db.query(User).filter(User.username == username).first()
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user

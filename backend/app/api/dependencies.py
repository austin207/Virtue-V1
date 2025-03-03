# backend/app/api/dependencies.py
from fastapi import Depends, HTTPException, status
from app.core.security import decode_access_token
from app.services.user_service import get_user_by_username

def get_current_user(token: str = Depends(lambda: None)):
    """
    Dependency to retrieve the current user based on the JWT token.
    In production, use OAuth2PasswordBearer to extract the token from the header.
    """
    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authenticated"
        )
    payload = decode_access_token(token)
    username: str = payload.get("sub")
    if username is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token"
        )
    user = get_user_by_username(username)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found"
        )
    return user

def get_current_admin(user=Depends(get_current_user)):
    """
    Dependency to ensure that the current user has admin privileges.
    """
    if not getattr(user, "is_admin", False):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Not enough permissions"
        )
    return user

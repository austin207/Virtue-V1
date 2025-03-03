# backend/app/api/routes/admin.py
from fastapi import APIRouter, Depends, HTTPException
from app.api.dependencies import get_current_admin

router = APIRouter()

@router.get("/stats")
async def admin_stats(admin=Depends(get_current_admin)):
    """
    Retrieve administrative statistics.
    This endpoint is protected and accessible only to admin users.
    """
    # Placeholder: Replace with real database queries and logic.
    stats = {
        "user_count": 100,      # Example static value
        "active_sessions": 5,     # Example static value
    }
    return stats

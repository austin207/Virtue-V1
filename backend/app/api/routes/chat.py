# backend/app/api/routes/chat.py
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from app.services.chat_service import process_chat_message
from app.api.dependencies import get_current_user

router = APIRouter()

# Request and Response models for the chat endpoint
class ChatRequest(BaseModel):
    session_id: str
    message: str

class ChatResponse(BaseModel):
    response: str

@router.post("/", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest, user=Depends(get_current_user)):
    """
    Endpoint to process a chat message and return the generated response.
    """
    try:
        response_text = await process_chat_message(request.session_id, request.message, user)
        return ChatResponse(response=response_text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

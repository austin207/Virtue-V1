# backend/app/llm/memory.py
"""
Simple in-memory context management for chat sessions.
For production, consider persisting session context in a database or cache.
"""
from collections import defaultdict

# In-memory store for chat histories
chat_memory = defaultdict(list)

def add_message(session_id: str, message: str, is_user: bool = True):
    """
    Add a chat message to the session history.
    """
    chat_memory[session_id].append({
        "is_user": is_user,
        "message": message,
    })

def get_session_history(session_id: str):
    """
    Retrieve the chat history for a given session.
    """
    return chat_memory.get(session_id, [])

# backend/app/services/chat_service.py
from app.llm import openai_client, prompt_templates, memory, models
from app.db.database import get_db
from app.db.models import ChatMessage
from sqlalchemy.orm import Session
import asyncio

async def process_chat_message(session_id: str, message: str, user):
    """
    Process the chat message by updating context, generating a response via LLM,
    and (optionally) saving the conversation to the database.
    """
    # Add the user's message to the in-memory session history
    memory.add_message(session_id, message, is_user=True)

    # Render the prompt using the default template
    prompt = prompt_templates.render_template("default", message=message)
    
    # Retrieve the model configuration
    model_config = models.get_model_config("default")
    
    # Get response from the OpenAI API (wrapped in asyncio.to_thread for blocking calls)
    response = await asyncio.to_thread(
        openai_client.get_openai_response, 
        prompt, 
        model_config["model"], 
        model_config["max_tokens"]
    )
    
    # Add the LLM response to the session history
    memory.add_message(session_id, response, is_user=False)

    # Optionally, save the chat interaction to the database.
    # In production, use a proper DB session dependency.
    # Example:
    # db: Session = next(get_db())
    # chat_entry = ChatMessage(session_id=session_id, message=message, response=response, user_id=user.id)
    # db.add(chat_entry)
    # db.commit()
    # db.refresh(chat_entry)
    
    return response

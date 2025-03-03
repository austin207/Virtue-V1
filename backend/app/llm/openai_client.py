# backend/app/llm/openai_client.py
import openai
from app.config import settings

# Configure OpenAI API key and base URL
openai.api_key = settings.OPENAI_API_KEY
openai.api_base = settings.OPENAI_API_BASE

async def get_openai_response(prompt: str, model: str = "text-davinci-003", max_tokens: int = 150):
    """
    Call the OpenAI API to generate a response based on the prompt.
    """
    try:
        response = openai.Completion.create(
            engine=model,
            prompt=prompt,
            max_tokens=max_tokens,
            temperature=0.7,
        )
        return response.choices[0].text.strip()
    except Exception as e:
        # In production, log the error details
        raise e

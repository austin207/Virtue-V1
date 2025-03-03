# backend/app/llm/models.py
"""
Configuration for available LLM models.
This can be expanded to support multiple models and parameters.
"""
model_configurations = {
    "default": {
        "model": "text-davinci-003",
        "max_tokens": 150,
        "temperature": 0.7,
    },
    # Add additional model configurations as needed
}

def get_model_config(name: str = "default"):
    """
    Retrieve the configuration for the specified model.
    """
    config = model_configurations.get(name)
    if not config:
        raise ValueError("Model configuration not found")
    return config

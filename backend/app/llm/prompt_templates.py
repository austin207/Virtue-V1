# backend/app/llm/prompt_templates.py
from jinja2 import Template

# Dictionary of prompt templates
templates = {
    "default": Template("You are a helpful assistant. {{ message }}"),
    # Additional templates can be added here
}

def render_template(template_name: str, **kwargs) -> str:
    """
    Render the specified prompt template with provided variables.
    """
    template = templates.get(template_name)
    if not template:
        raise ValueError("Template not found")
    return template.render(**kwargs)

import os

from dotenv import load_dotenv

DEFAULT_OPENAI_MODEL = "gpt-4.1-nano"


def get_openai_api_key():
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY not found in environment variables.")
    return api_key

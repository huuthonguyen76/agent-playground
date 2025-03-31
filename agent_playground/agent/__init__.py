import aisuite as ai

from dotenv import load_dotenv

load_dotenv()

ai_client = ai.Client()


def get_ai_client() -> ai.Client:
    """Get the global AI client instance.

    The client is initialized once when this module is imported and reused
    for all subsequent calls.

    Returns:
        ai.Client: The global AI client instance configured with environment settings.
    """
    return ai_client

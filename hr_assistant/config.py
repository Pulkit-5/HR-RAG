"""All settings for the app live here, in one place."""

import os
from dotenv import load_dotenv

load_dotenv()

# API KEYS
JINA_API_KEY = os.getenv("JINA_API_KEY")
PORTKEY_API_KEY = os.getenv("PORTKEY_API_KEY")

# GUARD MODEL
GUARD_MODEL_NAME = "gemini-3.1-flash-lite"

# TRACING
LANGSMITH_TRACING = os.getenv("LANGSMITH_TRACING", "false")
LANGSMITH_ENDPOINT = os.getenv("LANGSMITH_ENDPOINT")
LANGSMITH_API_KEY = os.getenv("LANGSMITH_API_KEY")
LANGSMITH_PROJECT = os.getenv("LANGSMITH_PROJECT")

# DATA
DATA_FILE_PATH = os.path.join("data", "hr_policy.txt")

# QDRANT
QDRANT_URL = os.getenv("QDRANT_URL")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
QDRANT_COLLECTION_NAME = os.getenv(
    "QDRANT_COLLECTION_NAME", "hr_policy"
)

# MODELS
LLM_MODEL_NAME = "gemini-3.1-flash-lite"
EMBEDDING_MODEL_NAME = "jina-embeddings-v2-base-en"

# TEXT SPLITTING
CHUNK_SIZE = 500
CHUNK_OVERLAP = 60

# RETRIEVAL
TOP_K_RESULTS = 3

# SYSTEM PROMPT
SYSTEM_PROMPT = (
    "You are a friendly HR assistant. Always use the search_hr_policy "
    "tool to look up facts before answering. If the answer isn't in "
    "the search results, say you don't know instead of guessing."
)


def check_api_keys() -> None:
    """Check required API keys and configuration."""

    if not PORTKEY_API_KEY:
        raise ValueError("Missing PORTKEY_API_KEY in your .env file.")

    if not JINA_API_KEY:
        raise ValueError("Missing JINA_API_KEY in your .env file.")

    if not QDRANT_URL or not QDRANT_API_KEY:
        raise ValueError(
            "Missing QDRANT_URL or QDRANT_API_KEY in your .env file."
        )
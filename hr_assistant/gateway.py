"""Route LLM calls through Portkey."""

from langchain_openai import ChatOpenAI
from portkey_ai import createHeaders, PORTKEY_GATEWAY_URL

from hr_assistant import config
from hr_assistant.logger import get_logger

logger = get_logger(__name__)

# Must match the Gemini provider slug configured in Portkey.
PRIMARY_PROVIDER = "hr-policy-rag"

from hr_assistant.config import PORTKEY_API_KEY
def get_gateway_llm(model_name=None):
    model_name = model_name or config.LLM_MODEL_NAME

    headers = createHeaders(
        api_key=config.PORTKEY_API_KEY,
        provider="@hr-policy-rag",
    )

    return ChatOpenAI(
        api_key=PORTKEY_API_KEY,
        base_url=PORTKEY_GATEWAY_URL,
        model=model_name,
        default_headers=headers,
        temperature=0,
    )
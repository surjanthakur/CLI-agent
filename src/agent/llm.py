from langchain_ollama import ChatOllama
from langchain.messages import HumanMessage, SystemMessage
from rich import print
from .prompt import system_prompt
from ..core.logging import logger


async def qwen_llm_response(query: str):
    try:
        llm = ChatOllama(
            model="qwen2.5-coder:3b",  # Which Ollama model to use
            temperature=0.2,  # Creativity (0 = deterministic, 1 = creative)
            num_ctx=8192,  # Context window
            num_predict=512,  # Maximum output tokens
            top_p=0.9,  # Sampling control
            repeat_penalty=1.1,  # Reduces repetition
        )
        messages = [
            SystemMessage(content=system_prompt()),
            HumanMessage(content=query),
        ]
        response_stream = llm.stream(messages)
        return response_stream
    except TimeoutError:
        print("[orange] timeout error might be the slow internet connection try again!")

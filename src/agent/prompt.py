from langchain_core.messages import SystemMessage


def system_prompt() -> SystemMessage:
    prompt = SystemMessage(content="you are a helpfull ai for learning.")
    return prompt

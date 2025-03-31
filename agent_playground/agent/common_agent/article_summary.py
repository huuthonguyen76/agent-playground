from agent_playground.agent.common_agent.prompts import AGENT_SUMMARY_PROMPT
from agent_playground.agent import get_ai_client


def agent_summary(content: str, model: str = "openai:gpt-4o-mini") -> str:
    ai_client = get_ai_client()

    messages = [
        {"role": "system", "content": AGENT_SUMMARY_PROMPT.format(content=content)},
    ]

    response = ai_client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0.3
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    content = "Hello, world!"
    summary = agent_summary(content)
    print(summary)

from agent_playground.agent.agent_article_writing.template import AGENT_ARTICLE_WRITING_PROMPT
from agent_playground.agent import get_ai_client


def agent_article_writing(content: str, model: str = "openai:gpt-4o") -> str:
    ai_client = get_ai_client()

    messages = [
        {"role": "system", "content": AGENT_ARTICLE_WRITING_PROMPT},
        {"role": "user", "content": f"Here is the Youtube transcript. Help me to turn it into an article, remember to follow the instructions: {content}"},
    ]

    response = ai_client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0.3
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    with open("agent_playground/agent/test_data/transcript.txt", "r") as f:
        transcript = f.read()

    article = agent_article_writing(transcript)
    print(article)

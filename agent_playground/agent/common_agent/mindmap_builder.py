from agent_playground.agent.common_agent.prompts import AGENT_MIND_MAP_PROMPT
from agent_playground.agent import get_ai_client


def agent_mindmap_builder(youtube_transcript: str, model: str = "openai:gpt-4o-mini") -> str:
    ai_client = get_ai_client()

    messages = [
        {"role": "system", "content": AGENT_MIND_MAP_PROMPT.format(youtube_transcript=youtube_transcript)},
    ]

    response = ai_client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0.3
    )

    markdown_mindmap = response.choices[0].message.content
    markdown_mindmap = markdown_mindmap.replace("```markdown", "").replace("```", "")
    return markdown_mindmap


if __name__ == "__main__":
    with open("agent_playground/agent/test_data/transcript.txt", "r") as f:
        transcript = f.read()

    mindmap = agent_mindmap_builder(transcript)
    print(mindmap)

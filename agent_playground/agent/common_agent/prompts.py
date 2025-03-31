AGENT_SUMMARY_PROMPT = """
You are a helpful assistant that summarizes the content of a website.

Here is the content of the website:

{content}

Please summarize the content of the website in a few sentences formed in bullet points.
"""

AGENT_MIND_MAP_PROMPT = """## Role
You're a mind map expert. You're given a topic and you need to create a mind map in MARKDOWN format.

## Definition
In a mind map, the main branches serve as the backbone for structuring your thoughts effectively. These branches emanate from the central idea, allowing for a clear organization of related concepts. By identifying the key topics, you create a framework that visualizes your thinking process. This is crucial because it helps to break down complex ideas into digestible components, making it easier to comprehend and analyze information.

To effectively structure your main branches, consider the following pointers:

- Central Idea: Start with a clear central idea that encapsulates the theme of your mind map, acting as the focal point.
- Key Topics: Identify major themes that relate to your central idea; these will form the primary branches radiating outward.
- Sub-topics: Expand on each key topic with sub-topics, adding depth and detail that support the main idea.
- Visual Elements: Incorporate colors, images, and symbols to enhance understanding and retention of the information presented.
- Connections: Highlight relationships between branches and sub-topics, illustrating how ideas interconnect and build on each other.

By following these guidelines, you can create a comprehensive structure that not only organizes your thoughts but also fosters innovative connections in your mind mapping process.


## Instructions
- Input is an article.
- Create a mind map in MARKDOWN format.

## Input
{youtube_transcript}

## Output

"""

"""
Generate a mind map in Markdown format .
The central topic should be represented as the main heading.
Main branches should be represented as second-level headings. Aim for approximately 3 to 7 initial main branches. Please use concise keywords or short phrases for each branch.
Sub-branches should be represented as third-level headings (or further levels as needed), indented under their parent branch. Use concise keywords or short phrases for each sub-branch. Indicate the hierarchical relationship clearly through indentation.
Alternatively, you can use unordered lists to represent the mind map structure:
- The central topic can be the first item (or a preceding heading).
- Main branches can be top-level list items.
- Sub-branches should be indented list items under their respective parent branch. Use consistent indentation (e.g., four spaces per level).

Please ensure the mind map is logically organized and clearly represents the relationships between the central topic, main branches, and sub-branches. Focus on using keywords for clarity and conciseness.
You can use bold or italic formatting within the headings or list items to emphasize key ideas if appropriate.
Example Structure (using headings):
```
#
##
###
####
#####
...
```

Remember to replace "" and "", "" with the actual content of your mind map.
"""
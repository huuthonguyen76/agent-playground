import gradio as gr

from agent_playground.agent.common_agent.article_summary import agent_summary
from agent_playground.agent.common_agent.mindmap_builder import agent_mindmap_builder
from agent_playground.agent.agent_article_writing.exec import agent_article_writing

from src.common.youtube import get_youtube_transribe
from .mindmap_html import html_text, iframe_html
from loguru import logger
from urllib.parse import urlparse, parse_qs


def get_mindmap_html(mindmap_text: str):
    return html_text.format(mindmap_text=mindmap_text)


def get_iframe_html(mindmap_text: str):
    mindmap_html = get_mindmap_html(mindmap_text)
    return iframe_html.format(html_text=mindmap_html)


mindmap_text = """# Trump Tariffs - March 4th

* **March 4th Implementation**
    * Mexico & Canada: 25% Tariffs
    * China: +10% Tariffs (Total 20%)
* **Justification**
    * "Illicit Drugs" from Mexico & Canada
    * Insufficient Border Policing
* **Announcement**
    * Truth Social Post
* **Reciprocal Tariffs**
    * April 2nd Date Remains
* **Confusion & Contradictions**
    * Initial Pause (Feb 3rd)
    * Hassett's Timeline (April 1st Study)
    * Market Reaction (Dow Jones)
* **White House Confirmation**
    * 20% Total for China
* **Trump's Tariff Agenda**
    * Core Second-Term Policy
    * Revenue Source
    * Threat Against Countries
    * Global Steel & Aluminum (25% - March 12th)
    * Reciprocal Tariffs (Feb 13th Memo)
        * Value-Added Taxes as Unfair Practice
* **Reporting**
    * CNBC (Megan Cassella, Eamon Javers)"""


def generate_mindmap(url: str):
    try:
        # Extract video ID from YouTube URL
        video_id = parse_qs(urlparse(url).query)['v'][0]

        # Get transcript and generate mindmap using agents
        video_transcript = get_youtube_transribe(video_id)
        article = agent_article_writing(video_transcript)
        mindmap_html = agent_mindmap_builder(article)
        
        return video_transcript, mindmap_html, article

    except Exception as e:
        logger.error(f"Error processing YouTube URL: {e}")
        return None


def create_summary_tab():
    with gr.Tab("Article Summary"):
        with gr.Row():
            with gr.Column(scale=1):
                url_text_box = gr.Textbox(label="Article URL", lines=1)
                submit_btn = gr.Button("Generate Summary")

            with gr.Column(scale=2):
                show_raw = gr.Checkbox(label="Show Raw Content", value=False)
                raw_content_text = gr.Markdown(label="Raw Content", visible=False)
                summary_text = gr.TextArea(label="Summary", visible=True)

                def toggle_raw_content(show):
                    return gr.update(visible=show)

                show_raw.change(
                    fn=toggle_raw_content,
                    inputs=[show_raw],
                    outputs=[raw_content_text]
                )

        submit_btn.click(
            fn=generate_mindmap,
            inputs=[url_text_box],
            outputs=[raw_content_text, summary_text]
        )


def create_interface():
    with gr.Blocks() as demo:
        gr.Markdown("# AI Agent Playground")

        with gr.Tabs():
            with gr.Tab("HTML View"):
                with gr.Row():
                    with gr.Column():
                        with gr.Row():
                            youtube_url = gr.Textbox(label="Youtube URL", lines=1)
                        
                        with gr.Row():
                            video_transcript = gr.TextArea(label="Video Transcript", value="", lines=10)
                        
                        with gr.Row():
                            article = gr.Markdown(label="Article", value="", container=True)

                        with gr.Row():
                            submit_btn = gr.Button("Generate Mindmap")

                        with gr.Row():
                            mindmap_html = gr.HTML(get_iframe_html(mindmap_text))
                        
                        with gr.Row():
                            mindmap_text_box = gr.TextArea(label="Mindmap Text", value=mindmap_text)

                    def update_mindmap_html(text):
                        return gr.update(value=get_iframe_html(text))

                    mindmap_text_box.change(
                        fn=update_mindmap_html,
                        inputs=[mindmap_text_box],
                        outputs=[mindmap_html]
                    )
                    
                    submit_btn.click(
                        fn=generate_mindmap,
                        inputs=[youtube_url],
                        outputs=[video_transcript, mindmap_text_box, article]
                    )

            create_summary_tab()
                
    return demo

if __name__ == "__main__":
    demo = create_interface()
    demo.launch()



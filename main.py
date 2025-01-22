import gradio as gr
from docling.document_converter import DocumentConverter


# Document parser
converter = DocumentConverter()

# Widgets
file_widget = gr.File(
    file_count = "single",
    file_types = ["pdf"],
    type = "filepath",
    label = "Source"
)
content_widget = gr.Textbox(
    label = "Source content",
)
script_widget = gr.Textbox(
    placeholder = "Script",
    label = "Script",
)
audio_widget = gr.Audio()


def parse_document(filepath: str):
    if filepath is None:
        return None
    result = converter.convert(filepath)
    return result.document.export_to_markdown()


def chat(*args, **kwargs):
    return 'Hello'


chat_widget = gr.ChatInterface(chat, examples = ["Summarize the key points in the document"])


with gr.Blocks() as demo:
    gr.Markdown("# NotebookLM")
    with gr.Row():

        with gr.Column():
            file_widget.render()
            content_widget.render()
            file_widget.change(parse_document, inputs = file_widget, outputs = content_widget)

        with gr.Column():
            chat_widget.render()

        with gr.Column():
            gr.Button(value = "Generate podcast")
            audio_widget.render()
            script_widget.render()


if __name__ == "__main__":
    demo.launch(server_port = 8100)
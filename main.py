import gradio as gr
from docling.document_converter import DocumentConverter


# Document parser
converter = DocumentConverter()

# Widgets
file_widget = gr.File(
    file_count = "single", # multiple,
    file_types = ["pdf"],
    type = "filepath",
    label = "Source"
)
submit_widget = gr.Button(
    value = "Submit",
    variant = "primary"
)
content_widget = gr.Textbox(
    placeholder = "Parsed document content",
    label = "Content",
)


def parse_document(filepath: str):
    result = converter.convert(filepath)
    return result.document.export_to_markdown()


with gr.Blocks() as demo:
    with gr.Column():
        file_widget.render()
        submit_widget.render()
        content_widget.render()
        submit_widget.click(parse_document, inputs = file_widget, outputs = content_widget)


if __name__ == "__main__":
    demo.launch(server_port = 8100)

# test = gr.Interface(
#     fn = parse_document,
#     inputs = [file_widget],
#     outputs = [content_widget]
# )
# test2 = gr.Text()
# demo = gr.TabbedInterface([test, test2], ["Hello World", "Bye World"])

    

#     gr.ChatInterface()
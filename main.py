import time
import gradio as gr

# Widgets
file_widget = gr.File(
    file_count = "single",
    file_types = [".txt"],
    type = "filepath",
    label = "Source"
)
content_widget = gr.Markdown()
generate_button_widget = gr.Button(
    value = "Generate"
)

def load_document(filepath: str):
    with open(filepath, "r") as f:
        doc = f.read()
    doc = doc.replace("Speaker 1:", "<b>Speaker 1:</b>").replace("Speaker 2:", "<b>Speaker 2:</b>")
    out = ""
    for char in doc:
        time.sleep(0.01)
        out += char
        yield out


with gr.Blocks() as demo:
    gr.Markdown("# NotebookLM")
    with gr.Row():

        with gr.Column():
            file_widget.render()
            generate_button_widget.render()
            generate_button_widget.click(
                inputs = [file_widget],
                outputs = [content_widget],
                fn = load_document,
            )

        with gr.Column():
            with gr.Tab("Script"):
                content_widget.render()


if __name__ == "__main__":
    demo.launch(server_port = 8100)
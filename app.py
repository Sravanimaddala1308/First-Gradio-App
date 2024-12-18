import gradio as gr

def greet():
    return 'Hi This is My First Gradio App'

demo=gr.Interface(
    fn=greet,
    inputs=[],
    outputs=["text"]
)

demo.launch()
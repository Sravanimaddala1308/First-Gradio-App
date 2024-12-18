import gradio as gr

def multiply(num1,num2):
    return num1*num2

demo=gr.Interface(
    fn=multiply,
    inputs=[gr.Number(label="Number1"),gr.Number(label="Number2")],
    outputs=[gr.Textbox(label="Result")],
    title="Multiplication App",
    description="Enter two numbers to multiply"

)

demo.launch()
import gradio as gr
from rag_inference import get_response

def chat_with_bot(question, chat_history):
    if not question.strip():
        return chat_history, chat_history

    answer, _ = get_response(question)
    chat_history.append((question, answer))
    return chat_history, chat_history

with gr.Blocks(title="Educational Assistant", theme=gr.themes.Soft()) as demo:
    gr.Markdown(
        """
        # 🎓 Educational RAG Chatbot
        Ask questions from your course notes and get accurate answers powered by a local LLM.
        """
    )

    chatbot = gr.Chatbot(label="📚 Assistant")
    question_input = gr.Textbox(
        label="Ask a Question",
        placeholder="e.g., What are Huffman trees?",
        lines=1
    )
    submit_btn = gr.Button("Get Answer")

    state = gr.State([])

    submit_btn.click(
        fn=chat_with_bot,
        inputs=[question_input, state],
        outputs=[chatbot, state]
    )

demo.launch()

import gradio as gr
from persistent_store import add_to_persistent_store, query_persistent_store
from quick_index import quick_pdf_query

with gr.Blocks(title="EduMate", theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 🎓 EduMate – Your Private AI Study Assistant")

    with gr.Tab("📘 Persistent Session (Semester Notes)"):
        gr.Markdown("Upload lecture notes chapter by chapter. All uploads will be stored in a FAISS index for ongoing queries.")

        with gr.Row():
            persistent_pdf_input = gr.File(file_types=[".pdf"], file_count="multiple", label="Upload Lecture PDFs")
        upload_status = gr.Label()
        upload_btn = gr.Button("Add Notes to Database")
        upload_btn.click(add_to_persistent_store, inputs=[persistent_pdf_input], outputs=[upload_status])

        persistent_question_input = gr.Textbox(label="Ask a Question (Search All Notes)")
        persistent_answer_output = gr.Markdown()
        ask_btn = gr.Button("Get Answer")
        ask_btn.click(query_persistent_store, inputs=[persistent_question_input], outputs=[persistent_answer_output])

    with gr.Tab("⚡ Quick Problem Solver (Temporary Session)"):
        gr.Markdown("Upload PDFs for instant answers. These will not be stored in the semester database.")

        with gr.Row():
            quick_pdf_input = gr.File(file_types=[".pdf"], file_count="multiple", label="Upload PDFs")
        quick_question_input = gr.Textbox(label="Ask a Question")
        quick_output = gr.Markdown()
        quick_btn = gr.Button("Get Answer")
        quick_btn.click(quick_pdf_query, inputs=[quick_pdf_input, quick_question_input], outputs=[quick_output])

demo.launch()

EduMate: A Private RAG-Powered Educational Assistant

EduMate is a local-first educational chatbot that helps students ask questions from their uploaded lecture notes using Retrieval-Augmented Generation (RAG). It now supports two modes: persistent sessions for semester-long study and quick sessions for instant document-based Q&A.

Features

Persistent Session:
Upload notes progressively during the semester
Automatically builds and updates a long-term FAISS knowledge base
Designed for continued learning and review

Quick Session:
Upload a single PDF and ask questions immediately
Uses a temporary vector store and does not persist data
Ideal for quick answers without affecting your main knowledge base

Powered by local LLMs such as FLAN-T5 or Mistral
Interactive and clean chat interface using Gradio
All queries and processing are handled locally without any internet requirement

Project Structure

Edumate/
│
├── app.py                 # Main interface with two tabs (Persistent and Quick)
├── document_utils.py      # Handles PDF/DOCX loading and splitting
├── llm_generate.py        # Generates answers using a local LLM
├── persistent_store.py    # Persistent vector indexing and querying
├── quick_index.py         # Temporary index for quick sessions
│
├── vector_store/          # Stores persistent FAISS index
├── logs/                  # Stores chat history as markdown logs
├── data/                  # User-provided PDFs (optional)
│
├── requirements.txt       # Project dependencies
├── README.md              # Project documentation
├── .gitignore             # Git exclusions

How to Run

1. Clone the repo and move into the folder
   git clone https://github.com/your-username/Edumate
   cd Edumate

2. Create and activate the environment
   conda create -n edumate python=3.10
   conda activate edumate

3. Install all required packages
   pip install -r requirements.txt

4. Run the chatbot app
   python app.py

You can access the chatbot at http://127.0.0.1:7860

License

This project is licensed under the MIT License.
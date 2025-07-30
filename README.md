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

<pre><code>```text Edumate/ ├── app.py # Main app with two tabs: Persistent & Quick session ├── document_utils.py # Handles PDF/DOCX parsing and chunking ├── llm_generate.py # Generates answers using local LLM (FLAN-T5/Mistral) ├── persistent_store.py # Adds and queries data in the persistent FAISS store ├── quick_index.py # Temporary FAISS store for quick PDF sessions ├── vector_store/ # Stores persistent FAISS index for semester sessions ├── data/ # (Optional) Folder where users can store uploaded notes ├── logs/ # Markdown log of chat sessions (auto-generated) ├── README.md # Project overview and instructions ├── requirements.txt # All dependencies └── .gitignore # Standard Git ignore rules ```</code></pre>

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
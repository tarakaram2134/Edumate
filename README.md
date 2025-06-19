
# EduMate – A Private RAG-Powered Educational Assistant 🧠📚

EduMate is an intelligent, local-first educational assistant that helps you query your course notes using state-of-the-art Retrieval-Augmented Generation (RAG). Powered by a local language model and vector search, EduMate provides accurate, contextual answers without needing internet access or external APIs.

---

## 🚀 Features

- 🔍 Ask questions from your uploaded lecture notes (PDFs)
- 🧠 Retrieves relevant context using FAISS vector search
- 🤖 Generates answers using locally run LLMs (FLAN-T5, Mistral)
- 📄 Clean, chat-style interface built with Gradio
- 💾 Saves all Q&A to Markdown logs
- 🔐 Runs entirely offline — no data leaves your machine

---

## 📁 Folder Structure

```
EduMate/
├── app.py                 # Gradio UI
├── test_qa.py             # Script interface for testing
├── rag_inference.py       # Core inference logic
├── qa_chain.py            # Vector retrieval layer
├── llm_generate.py        # Model generation layer
├── rag_pipeline.py        # FAISS index builder
├── document_loader.py     # Loads & parses PDFs
├── index_notes.py         # Runs PDF indexing
├── sample_notes/          # Sample PDFs for demo
├── vector_store/          # Auto-generated FAISS index
├── logs/                  # Saved Q&A interactions
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🛠️ Installation

```bash
# 1. Clone the repo
git clone https://github.com/yourusername/edumate.git
cd edumate

# 2. Create and activate your environment (recommended)
conda create -n edumate python=3.10 -y
conda activate edumate

# 3. Install dependencies
pip install -r requirements.txt
```

---

## 📚 Usage

### ▶️ Index your PDFs
Place your lecture PDFs in `sample_notes/` and run:

```bash
python index_notes.py
```

### 💬 Launch the Chat Interface

```bash
python app.py
```

Open `http://127.0.0.1:7860` in your browser to interact with EduMate.

---

## ✨ Example Question

```
What are Huffman trees?
```

EduMate will search your notes, retrieve relevant chunks, and generate a helpful answer.

---

## 🧠 Models Supported

- `google/flan-t5-base` / `flan-t5-large` (default)
- `mistralai/Mistral-7B-Instruct` (optional, with GPU support)

---

## ✅ TODOs (for future versions)

- [ ] PDF drag-and-drop uploader
- [ ] Per-session chat history viewer
- [ ] Fine-tuned LLM adapter (LoRA or QLoRA)
- [ ] Web deployment via Hugging Face Spaces or Streamlit Cloud

---

## 🧑‍💻 Author

**Taraka Ram Donepudi**  
Master’s in Computer Science  
Project: AI/ML-Powered Education Tool

---

## 🛡 License

MIT License – free to use, fork, and improve!

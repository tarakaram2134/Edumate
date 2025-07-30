import os
from langchain_community.vectorstores import FAISS as LCFAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from document_utils import process_pdfs_to_chunks
from llm_generate import generate_answer

PERSISTENT_INDEX_DIR = "vector_store"

def add_to_persistent_store(pdf_files):
    """Processes PDFs, embeds chunks, and appends them to the persistent FAISS store."""
    chunks = process_pdfs_to_chunks(pdf_files)
    if not chunks:
        return "No valid text found in PDFs."

    embeddings = HuggingFaceEmbeddings()

    os.makedirs(PERSISTENT_INDEX_DIR, exist_ok=True)

    if os.path.exists(os.path.join(PERSISTENT_INDEX_DIR, "index.faiss")):
        db = LCFAISS.load_local(PERSISTENT_INDEX_DIR, embeddings, allow_dangerous_deserialization=True)
        new_db = LCFAISS.from_texts(chunks, embeddings)
        db.merge_from(new_db)
        db.save_local(PERSISTENT_INDEX_DIR)
    else:
        db = LCFAISS.from_texts(chunks, embeddings)
        db.save_local(PERSISTENT_INDEX_DIR)

    return f"Added {len(chunks)} chunks to the persistent notes database."

def query_persistent_store(question):
    """Searches the persistent FAISS index and generates an answer."""
    if not os.path.exists(PERSISTENT_INDEX_DIR):
        return "No notes found. Please upload PDFs first."

    embeddings = HuggingFaceEmbeddings()
    db = LCFAISS.load_local(PERSISTENT_INDEX_DIR, embeddings, allow_dangerous_deserialization=True)
    docs = db.similarity_search(question, k=4)
    context = "\n\n---\n\n".join([d.page_content for d in docs])
    answer = generate_answer(context, question)
    return f"**Answer:** {answer}\n\n**Context Used:**\n{context}"

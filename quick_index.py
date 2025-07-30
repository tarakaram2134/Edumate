import faiss
from sentence_transformers import SentenceTransformer
from document_utils import process_pdfs_to_chunks
from llm_generate import generate_answer

embedder = SentenceTransformer("all-MiniLM-L6-v2")

def quick_pdf_query(pdf_files, question):
    """Builds a temporary FAISS index from PDFs and answers the question."""
    chunks = process_pdfs_to_chunks(pdf_files)
    if not chunks:
        return "No text found in the uploaded PDFs."

    embeddings = embedder.encode(chunks, show_progress_bar=False)
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)

    query_vector = embedder.encode([question])
    D, I = index.search(query_vector, k=4)
    retrieved_chunks = [chunks[i] for i in I[0]]
    context = "\n\n---\n\n".join(retrieved_chunks)
    answer = generate_answer(context, question)
    return f"**Answer:** {answer}\n\n**Context Used:**\n{context}"

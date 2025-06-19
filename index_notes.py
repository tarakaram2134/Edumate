from document_loader import load_documents
from rag_pipeline import build_vector_store

docs = load_documents("../data/notes/")
build_vector_store(docs)
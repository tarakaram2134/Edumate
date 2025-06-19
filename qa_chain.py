import faiss
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
# Load vector DB
INDEX_PATH = "vector_store/docs.index"
META_PATH = "vector_store/metadata.pkl"
embed_model = SentenceTransformer('all-MiniLM-L6-v2')

# Load index and metadata
index = faiss.read_index(INDEX_PATH)
with open(META_PATH, "rb") as f:
    texts, metadatas = pickle.load(f)

def query_notes(question, k=4):
    # Load existing vector store
    db = FAISS.load_local("vector_store", HuggingFaceEmbeddings(), allow_dangerous_deserialization=True)
    
    # Perform similarity search
    docs = db.similarity_search(question, k=k)

    # Combine content and get sources
    combined_content = "\n\n---\n\n".join(doc.page_content for doc in docs)
    sources = list({doc.metadata.get('source', 'N/A') for doc in docs})

    return combined_content, sources
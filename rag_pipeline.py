from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter

def build_vector_store(documents, persist_path="vector_store"):
    print(f"📄 Total chunks: {len(documents)}")

    # split docs
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    splits = splitter.split_documents(documents)

    # embed & save
    vectorstore = FAISS.from_documents(splits, HuggingFaceEmbeddings())
    vectorstore.save_local(persist_path)
    print(f"✅ Vector store saved in '{persist_path}/'")

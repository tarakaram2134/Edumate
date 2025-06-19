import os
from PyPDF2 import PdfReader
from typing import List, Tuple
from PyPDF2 import PdfReader
from langchain.docstore.document import Document

def load_documents(folder_path):
    documents = []

    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(folder_path, filename)
            reader = PdfReader(pdf_path)

            for i, page in enumerate(reader.pages):
                text = page.extract_text()
                if text:
                    doc = Document(
                        page_content=text,
                        metadata={"source": filename, "page": i + 1}
                    )
                    documents.append(doc)

    return documents

def load_pdf_text(file_path: str) -> str:
    text = ""
    reader = PdfReader(file_path)
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text

def load_documents_from_folder(folder_path: str) -> List[Tuple[str, str]]:
    """
    Returns a list of tuples (text_chunk, source_filename)
    """
    documents = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):
            full_path = os.path.join(folder_path, filename)
            pdf_text = load_pdf_text(full_path)
            documents.append((pdf_text, filename))
    return documents

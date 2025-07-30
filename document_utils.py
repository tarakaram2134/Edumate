from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)

def process_pdfs_to_chunks(pdf_files):
    """Extracts text and splits it into chunks from given PDFs."""
    all_text = ""
    for file in pdf_files:
        reader = PdfReader(file.name)
        for page in reader.pages:
            text = page.extract_text()
            if text:
                all_text += text + "\n"
    return splitter.split_text(all_text)

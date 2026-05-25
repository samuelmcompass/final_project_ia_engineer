import os

from langchain_community.document_loaders import (
    TextLoader,
    PyPDFLoader,
    PyMuPDFLoader
)

#calculate file size
def size_file(file_path):
    if os.path.exists(file_path):

        size_bytes = os.path.getsize(file_path)
        size_kb = size_bytes / 1024
        size_mb = size_bytes / (1024 * 1024)

        print(f"Path: {file_path}")
        print(f"Size (bytes): {size_bytes}")
        print(f"Size (KB): {size_kb:.2f}")
        print(f"Size (MB): {size_mb:.2f}")

    else:

        print("File not found.")

#load txt file
def load_txt_document(file_path):

    loader = TextLoader(file_path)

    documents = loader.load()

    return documents

#load pdf file
def load_pdf_document(file_path):

    loader = PyMuPDFLoader(file_path)

    documents = loader.load()

    return documents
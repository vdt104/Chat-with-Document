from langchain_community.document_loaders import PyPDFLoader, TextLoader, CSVLoader, Docx2txtLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from app.chat.vector_stores.pinecone import vector_store
import os

def create_embeddings_for_pdf(pdf_id: str, file_path: str, file_extension: str):
    """
    Generate and store embeddings for the given file

    1. Extract text from the specified file.
    2. Divide the extracted text into manageable chunks.
    3. Generate an embedding for each chunk.
    4. Persist the generated embeddings.

    :param pdf_id: The unique identifier for the file.
    :param file_path: The file path to the file.
    :param file_extension: The file extension of the file.

    Example Usage:

    create_embeddings_for_file('123456', '/path/to/file', '.pdf')
    """

    textsplitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
    )

    if file_extension == '.pdf':
        loader = PyPDFLoader(file_path)
        docs = loader.load_and_split(textsplitter)
    elif file_extension == '.txt':
        loader = TextLoader(file_path)
        docs = loader.load_and_split(textsplitter)
    elif file_extension == '.csv':
        loader = CSVLoader(file_path)
        docs = loader.load_and_split(textsplitter)
    elif file_extension == '.docx':
        loader = Docx2txtLoader(file_path)
        docs = loader.load_and_split(textsplitter)
    else:
        raise ValueError(f"Unsupported file type: {file_extension}")

    for doc in docs:
        doc.metadata = {
            "page": doc.metadata.get("page", 1) if hasattr(doc, 'metadata') else 1,
            "text": doc.page_content,
            "pdf_id": pdf_id,
        }


    vector_store.add_documents(docs)
import os
import base64
import fitz  # PyMuPDF
from dotenv import load_dotenv
from fastapi import FastAPI, Request
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document

load_dotenv()

# Inicializa embeddings e ChromaDB
embedding = OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY"))

vectorstore = Chroma(
    embedding_function=embedding,
    persist_directory=os.getenv("CHROMA_DB_DIR")
)

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "AutoFácil RAG API pronta!"}


# Função para extrair texto de PDF a partir de bytes
def extract_text_from_pdf_bytes(pdf_bytes: bytes) -> str:
    text = ""
    with fitz.open(stream=pdf_bytes, filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    return text


@app.post("/webhook/ingest")
async def ingest_file(request: Request):
    body = await request.json()
    filename = body.get("filename", "desconhecido.txt")
    content_base64 = body.get("content", "")

    try:
        raw_bytes = base64.b64decode(content_base64)
    except Exception:
        return {"status": "erro", "mensagem": "Base64 inválido."}

    # Detecta tipo do arquivo
    if filename.lower().endswith(".pdf"):
        text = extract_text_from_pdf_bytes(raw_bytes)
    else:
        try:
            text = raw_bytes.decode("utf-8")
        except UnicodeDecodeError:
            return {"status": "erro", "mensagem": "Não foi possível decodificar o arquivo como texto."}

    # Divide em chunks
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_text(text)

    documents = [
        Document(page_content=chunk, metadata={"source": filename})
        for chunk in chunks
    ]

    vectorstore.add_documents(documents)

    return {
        "status": "sucesso",
        "arquivo": filename,
        "chunks_indexados": len(documents)
    }

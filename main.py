import os
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from fastapi import FastAPI

load_dotenv()

embedding = OpenAIEmbeddings(
    openai_api_key=os.getenv("OPENAI_API_KEY")
)

vectorstore = Chroma(
    embedding_function=embedding,
    persist_directory=os.getenv("CHROMA_DB_DIR")
)

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "AutoFácil RAG API pronta!"}

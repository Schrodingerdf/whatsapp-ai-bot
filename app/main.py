from fastapi import FastAPI
from app.config import APP_NAME, APP_VERSION

app = FastAPI(
    title=APP_NAME,
    version=APP_VERSION,
    description="Chatbot para WhatsApp con IA"
)


@app.get("/")
def home():
    return {
        "status": "online",
        "project": APP_NAME,
        "version": APP_VERSION
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
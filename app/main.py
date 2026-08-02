from fastapi import FastAPI

app = FastAPI(
    title="WhatsApp AI Bot",
    description="Chatbot para WhatsApp con IA",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "status": "online",
        "project": "WhatsApp AI Bot",
        "version": "1.0.0"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
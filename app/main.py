from fastapi import FastAPI

from app.config import APP_NAME, APP_VERSION
from app.routers.health import router as health_router
from app.routers.webhook import router as webhook_router

app = FastAPI(
    title=APP_NAME,
    version=APP_VERSION,
    description="Chatbot para WhatsApp con IA"
)

app.include_router(health_router)
app.include_router(webhook_router)
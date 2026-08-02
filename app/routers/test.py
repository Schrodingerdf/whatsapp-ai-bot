from fastapi import APIRouter

from app.services.whatsapp import WhatsAppService
from app.services.gemini import GeminiService

router = APIRouter(prefix="/test", tags=["Test"])

whatsapp = WhatsAppService()
gemini = GeminiService()


@router.get("/send")
def send():

    response = whatsapp.send_text(
        to="51950700696",
        message="🚀 Hola, este mensaje fue enviado desde mi chatbot."
    )

    return response


@router.get("/gemini")
def test_gemini():

    response = gemini.ask(
        "¿Qué servicios ofrece Kusi Celebration?"
    )

    return {
        "response": response
    }

@router.get("/models")
def list_models():

    models = []

    for model in gemini.client.models.list():
        models.append(model.name)

    return {
        "models": models
    }
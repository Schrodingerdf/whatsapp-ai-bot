from fastapi import APIRouter
from app.services.whatsapp import WhatsAppService

router = APIRouter(prefix="/test", tags=["Test"])

whatsapp = WhatsAppService()


@router.get("/send")
def send():

    response = whatsapp.send_text(
        to="51950700696",
        message="🚀 Hola, este mensaje fue enviado desde mi chatbot."
    )

    return response
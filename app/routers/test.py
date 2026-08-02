from fastapi import APIRouter
from app.services.whatsapp import WhatsAppService

router = APIRouter(prefix="/test", tags=["Test"])

whatsapp = WhatsAppService()


@router.get("/send")
def send():

    response = whatsapp.send_text(
        to="TU_NUMERO_CON_CODIGO_PAIS",
        message="🚀 Hola Diego, este mensaje fue enviado desde tu propio chatbot."
    )

    return response
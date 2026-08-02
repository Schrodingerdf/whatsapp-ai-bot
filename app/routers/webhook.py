from fastapi import APIRouter, Request, Query
from fastapi.responses import PlainTextResponse

from app.config import VERIFY_TOKEN
from app.services.whatsapp import WhatsAppService
from app.services.chatbot import ChatBot

router = APIRouter(
    prefix="/webhook",
    tags=["WhatsApp Webhook"]
)

whatsapp = WhatsAppService()
chatbot = ChatBot()


@router.get("")
async def verify_webhook(
    hub_mode: str = Query(None, alias="hub.mode"),
    hub_verify_token: str = Query(None, alias="hub.verify_token"),
    hub_challenge: str = Query(None, alias="hub.challenge"),
):

    if hub_mode == "subscribe" and hub_verify_token == VERIFY_TOKEN:
        return PlainTextResponse(content=hub_challenge)

    return PlainTextResponse("Token invalido", status_code=403)


@router.post("")
async def receive_message(request: Request):

    body = await request.json()

    try:

        value = body["entry"][0]["changes"][0]["value"]

        # Si no es un mensaje, no hacemos nada
        if "messages" not in value:
            return {"status": "ok"}

        message = value["messages"][0]

        # Solo responder mensajes de texto
        if message["type"] != "text":
            return {"status": "ok"}

        phone = message["from"]
        user_message = message["text"]["body"]

        print("=" * 60)
        print("USUARIO:", phone)
        print("MENSAJE:", user_message)
        print("=" * 60)

        # Obtener respuesta del chatbot
        response = chatbot.process(user_message)

        # Enviar respuesta por WhatsApp
        whatsapp.send_text(
            to=phone,
            message=response
        )

    except Exception as e:
        print("=" * 60)
        print("ERROR EN WEBHOOK")
        print(e)
        print("=" * 60)

    return {"status": "ok"}
from fastapi import APIRouter, Request, Query
from fastapi.responses import PlainTextResponse

from app.config import VERIFY_TOKEN
from app.services.whatsapp import WhatsAppService

router = APIRouter(
    prefix="/webhook",
    tags=["WhatsApp Webhook"]
)

whatsapp = WhatsAppService()


@router.get("")
async def verify_webhook(
    hub_mode: str = Query(None, alias="hub.mode"),
    hub_verify_token: str = Query(None, alias="hub.verify_token"),
    hub_challenge: str = Query(None, alias="hub.challenge"),
):

    if hub_mode == "subscribe" and hub_verify_token == VERIFY_TOKEN:
        return PlainTextResponse(content=hub_challenge)

    return PlainTextResponse("Token inválido", status_code=403)


@router.post("")
print("POST /webhook RECIBIDO")
async def receive_message(request: Request):

    body = await request.json()

    print("=" * 60)
    print("MENSAJE RECIBIDO")
    print(body)
    print("=" * 60)

    try:
        value = body["entry"][0]["changes"][0]["value"]

        if "messages" not in value:
            return {"status": "ok"}

        message = value["messages"][0]
        phone = message["from"]

        whatsapp.send_text(
            to=phone,
            message="👋 Hola, este mensaje fue enviado automáticamente desde tu chatbot."
        )

    except Exception as e:
        print(f"Error: {e}")

    return {"status": "ok"}
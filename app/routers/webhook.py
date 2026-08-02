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

    return PlainTextResponse("Token invalido", status_code=403)


@router.post("")
async def receive_message(request: Request):

    body = await request.json()

    print(body)

    try:
        value = body["entry"][0]["changes"][0]["value"]

        if "messages" in value:

            message = value["messages"][0]
            from_number = message["from"]
            text = message["text"]["body"]

            print("MENSAJE:", text)

            whatsapp.send_text(
                to=from_number,
                message=f"👋 Hola, recibí tu mensaje: {text}"
            )

    except Exception as e:
        print("ERROR:", e)

    return {"status": "ok"}
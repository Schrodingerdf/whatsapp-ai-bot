from fastapi import APIRouter, Request, Query
from fastapi.responses import PlainTextResponse

from app.config import VERIFY_TOKEN

router = APIRouter(
    prefix="/webhook",
    tags=["WhatsApp Webhook"]
)


@router.get("")
async def verify_webhook(
    hub_mode: str = Query(None, alias="hub.mode"),
    hub_verify_token: str = Query(None, alias="hub.verify_token"),
    hub_challenge: str = Query(None, alias="hub.challenge"),
):

    print("========== GET WEBHOOK ==========")
    print("hub_mode:", hub_mode)
    print("hub_verify_token:", hub_verify_token)
    print("VERIFY_TOKEN:", VERIFY_TOKEN)
    print("=================================")

    if hub_mode == "subscribe" and hub_verify_token == VERIFY_TOKEN:
        print("WEBHOOK VERIFICADO")
        return PlainTextResponse(content=hub_challenge)

    print("TOKEN INVALIDO")
    return PlainTextResponse("Token invalido", status_code=403)


@router.post("")
async def receive_message(request: Request):

    print("")
    print("🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥")
    print("POST /webhook RECIBIDO")
    print("🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥")

    body = await request.json()

    print("")
    print("PAYLOAD COMPLETO:")
    print(body)
    print("")

    return {"status": "ok"}
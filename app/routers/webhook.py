from fastapi import APIRouter, Request, Query
from fastapi.responses import PlainTextResponse
from app.config import VERIFY_TOKEN

router = APIRouter(prefix="/webhook", tags=["WhatsApp Webhook"])


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
async def receive_message(request: Request):

    body = await request.json()

    print("=" * 60)
    print("📩 MENSAJE RECIBIDO")
    print(body)
    print("=" * 60)

    return {"status": "ok"}
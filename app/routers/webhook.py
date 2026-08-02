from fastapi import APIRouter, Request
from fastapi.responses import PlainTextResponse

router = APIRouter(prefix="/webhook", tags=["WhatsApp Webhook"])


# ==========================================
# Verificación del Webhook (Meta)
# ==========================================
@router.get("")
async def verify_webhook(
    hub_mode: str = None,
    hub_verify_token: str = None,
    hub_challenge: str = None,
):

    VERIFY_TOKEN = "mi_token_super_secreto"

    if hub_mode == "subscribe" and hub_verify_token == VERIFY_TOKEN:
        return PlainTextResponse(content=hub_challenge)

    return {"error": "Token inválido"}


# ==========================================
# Recepción de mensajes
# ==========================================
@router.post("")
async def receive_message(request: Request):

    body = await request.json()

    print("\n" + "=" * 60)
    print("📩 MENSAJE RECIBIDO")
    print("=" * 60)
    print(body)
    print("=" * 60 + "\n")

    return {"status": "ok"}
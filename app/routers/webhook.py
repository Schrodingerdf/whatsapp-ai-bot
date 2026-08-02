@router.post("")
async def receive_message(request: Request):

    body = await request.json()

    print("=" * 60)
    print(body)
    print("=" * 60)

    try:

        value = body["entry"][0]["changes"][0]["value"]

        if "messages" not in value:
            return {"status": "ok"}

        message = value["messages"][0]

        phone = message["from"]

        from app.services.whatsapp import WhatsAppService

        whatsapp = WhatsAppService()

        whatsapp.send_text(
            to=phone,
            message="👋 Hola, este mensaje fue enviado automáticamente desde tu chatbot."
        )

    except Exception as e:

        print(e)

    return {"status": "ok"}
import requests

from app.config import WHATSAPP_TOKEN, PHONE_NUMBER_ID


class WhatsAppService:

    def send_text(self, to: str, message: str):

        url = f"https://graph.facebook.com/v23.0/{PHONE_NUMBER_ID}/messages"

        headers = {
            "Authorization": f"Bearer {WHATSAPP_TOKEN}",
            "Content-Type": "application/json",
        }

        payload = {
            "messaging_product": "whatsapp",
            "to": to,
            "type": "text",
            "text": {
                "body": message
            }
        }

        print("=" * 60)
        print("ENVIANDO MENSAJE A WHATSAPP")
        print("PHONE_NUMBER_ID:", repr(PHONE_NUMBER_ID))
        print("TOKEN EXISTE:", bool(WHATSAPP_TOKEN))
        print("TOKEN PRIMEROS 10:", WHATSAPP_TOKEN[:10] if WHATSAPP_TOKEN else "VACIO")
        print("URL:", url)
        print("DESTINO:", to)
        print("PAYLOAD:", payload)
        print("=" * 60)

        response = requests.post(
            url,
            headers=headers,
            json=payload
        )

        print("=" * 60)
        print("RESPUESTA DE META")
        print("STATUS:", response.status_code)
        print("BODY:", response.text)
        print("=" * 60)

        try:
            return response.json()
        except Exception:
            return {
                "status": response.status_code,
                "body": response.text
            }
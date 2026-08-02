import requests

from app.config import (
    WHATSAPP_TOKEN,
    PHONE_NUMBER_ID,
    TARJETAS_AUDIO_ID
)


class WhatsAppService:

    # ==================================================
    # ENVIAR TEXTO
    # ==================================================
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
        print("ENVIANDO TEXTO")
        print("DESTINO:", to)

        response = requests.post(
            url,
            headers=headers,
            json=payload
        )

        print("STATUS:", response.status_code)
        print(response.text)
        print("=" * 60)

        return response.json()

    # ==================================================
    # ENVIAR AUDIO
    # ==================================================
    def send_audio(self, to: str):

        url = f"https://graph.facebook.com/v23.0/{PHONE_NUMBER_ID}/messages"

        headers = {
            "Authorization": f"Bearer {WHATSAPP_TOKEN}",
            "Content-Type": "application/json",
        }

        payload = {
            "messaging_product": "whatsapp",
            "to": to,
            "type": "audio",
            "audio": {
                "id": TARJETAS_AUDIO_ID
            }
        }

        print("=" * 60)
        print("ENVIANDO AUDIO")
        print("DESTINO:", to)
        print("MEDIA_ID:", TARJETAS_AUDIO_ID)

        response = requests.post(
            url,
            headers=headers,
            json=payload
        )

        print("STATUS:", response.status_code)
        print(response.text)
        print("=" * 60)

        return response.json()
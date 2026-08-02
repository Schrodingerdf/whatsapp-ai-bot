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

        response = requests.post(
            url,
            headers=headers,
            json=payload
        )

        print(response.status_code)
        print(response.text)

        return response.json()
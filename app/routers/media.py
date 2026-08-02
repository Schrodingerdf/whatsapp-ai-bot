from fastapi import APIRouter
import requests

from app.config import WHATSAPP_TOKEN, PHONE_NUMBER_ID

router = APIRouter(
    prefix="/media",
    tags=["Media"]
)


@router.get("/upload-audio")
def upload_audio():

    url = f"https://graph.facebook.com/v23.0/{PHONE_NUMBER_ID}/media"

    headers = {
        "Authorization": f"Bearer {WHATSAPP_TOKEN}"
    }

    with open("media/Jacky_audio.mp3", "rb") as audio:

        files = {
            "file": ("Jacky_audio.mp3", audio, "audio/mpeg")
        }

        data = {
            "messaging_product": "whatsapp"
        }

        response = requests.post(
            url,
            headers=headers,
            files=files,
            data=data
        )

    return response.json()
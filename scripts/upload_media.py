import os
import sys
import requests
from pathlib import Path
from dotenv import load_dotenv

# Cargar el .env desde la raíz del proyecto
load_dotenv(Path(__file__).resolve().parent.parent / ".env")

WHATSAPP_TOKEN = os.getenv("WHATSAPP_TOKEN")
PHONE_NUMBER_ID = os.getenv("PHONE_NUMBER_ID")

print("=" * 60)
print("CONFIG")
print("PHONE_NUMBER_ID:", PHONE_NUMBER_ID)
print("TOKEN EXISTE:", bool(WHATSAPP_TOKEN))
print("=" * 60)

if len(sys.argv) != 2:
    print("Uso:")
    print("python scripts/upload_media.py media/Jacky_audio.mp3")
    exit()

archivo = sys.argv[1]

url = f"https://graph.facebook.com/v23.0/{PHONE_NUMBER_ID}/media"

headers = {
    "Authorization": f"Bearer {WHATSAPP_TOKEN}"
}

print("=" * 60)
print("SUBIENDO ARCHIVO")
print("Archivo:", archivo)
print("URL:", url)
print("=" * 60)

with open(archivo, "rb") as f:

    files = {
        "file": (
            os.path.basename(archivo),
            f,
            "audio/mpeg"
        )
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

print("=" * 60)
print("STATUS:", response.status_code)
print("RESPUESTA:")
print(response.text)
print("=" * 60)
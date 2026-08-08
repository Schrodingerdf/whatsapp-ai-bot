from dotenv import load_dotenv
import os

load_dotenv()

APP_NAME = os.getenv("APP_NAME", "WhatsApp AI Bot")
APP_VERSION = os.getenv("APP_VERSION", "1.0.0")
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")

VERIFY_TOKEN = os.getenv("VERIFY_TOKEN", "mi_token_super_secreto")

WHATSAPP_TOKEN = os.getenv("WHATSAPP_TOKEN", "")
PHONE_NUMBER_ID = os.getenv("PHONE_NUMBER_ID", "")
ASESOR_PHONE = os.getenv("ASESOR_PHONE", "")
ASESOR_LINK = os.getenv("ASESOR_LINK", "")
TARJETAS_AUDIO_ID = os.getenv("TARJETAS_AUDIO_ID", "")
REMINDER_SECONDS = int(os.getenv("REMINDER_SECONDS", "180"))

# ==========================
# GEMINI
# ==========================

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-flash-lite")
SESSION_TIMEOUT_MINUTES = int(
    os.getenv("SESSION_TIMEOUT_MINUTES", "30")
)

print("=" * 60)
print("CONFIG CARGADA")
print("APP_NAME:", APP_NAME)
print("PHONE_NUMBER_ID:", repr(PHONE_NUMBER_ID))
print("TOKEN EXISTE:", bool(WHATSAPP_TOKEN))
print("TOKEN PRIMEROS 10:", WHATSAPP_TOKEN[:10] if WHATSAPP_TOKEN else "VACIO")
print("GEMINI:", bool(GEMINI_API_KEY))
print("=" * 60)
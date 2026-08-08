from google import genai

from app.config import GEMINI_API_KEY, GEMINI_MODEL

from app.services.prompts import (
    SYSTEM_PROMPT,
    CLASSIFICATION_PROMPT
)

from app.services.ai_result import AIResult


class GeminiService:

    def __init__(self):

        self.client = genai.Client(
            api_key=GEMINI_API_KEY
        )

        self.model = GEMINI_MODEL

    # ==================================================
    # RESPUESTA DE TEXTO
    # ==================================================

    def ask(self, question: str) -> str:

        try:

            response = self.client.models.generate_content(
                model=self.model,
                contents=f"""
{SYSTEM_PROMPT}

Pregunta del cliente:

{question}
"""
            )

            return response.text

        except Exception as e:

            print("=" * 60)
            print("ERROR GEMINI")
            print(e)
            print("=" * 60)

            return (
                "Lo siento 😥\n\n"
                "En este momento no puedo responder.\n"
                "Inténtalo nuevamente en unos minutos."
            )

    # ==================================================
    # CLASIFICACIÓN ESTRUCTURADA
    # ==================================================

    def classify(self, user_message: str) -> AIResult:

        prompt = f"""
{CLASSIFICATION_PROMPT}

MENSAJE DEL CLIENTE:

{user_message}
"""

        try:

            response = self.client.models.generate_content(
                model=self.model,
                contents=prompt,
                config={
                    "response_mime_type": "application/json",
                    "response_schema": AIResult,
                },
            )

            result = AIResult.model_validate_json(
                response.text
            )

            print("=" * 60)
            print("GEMINI - CLASIFICACION")
            print("MENSAJE:", user_message)
            print("RESULTADO:", result.model_dump())
            print("=" * 60)

            return result

        except Exception as e:

            print("=" * 60)
            print("ERROR CLASIFICANDO CON GEMINI")
            print(e)
            print("=" * 60)

            # Si Gemini falla, derivamos al asesor
            # en lugar de inventar una respuesta.
            return AIResult(
                requiere_asesor=True
            )
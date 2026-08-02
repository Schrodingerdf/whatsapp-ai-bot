from google import genai

from app.config import GEMINI_API_KEY, GEMINI_MODEL
from app.services.prompts import SYSTEM_PROMPT


class GeminiService:

    def __init__(self):

        self.client = genai.Client(
            api_key=GEMINI_API_KEY
        )

        self.model = GEMINI_MODEL

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
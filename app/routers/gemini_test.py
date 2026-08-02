from fastapi import APIRouter

from app.services.gemini import GeminiService

router = APIRouter(
    prefix="/gemini",
    tags=["Gemini"]
)

gemini = GeminiService()


@router.get("/test")
def test():

    response = gemini.ask(
        "¿Qué servicios ofrece Kusi Celebration?"
    )

    return {
        "response": response
    }
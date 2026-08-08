from fastapi import APIRouter

from app.services.gemini import GeminiService


router = APIRouter(
    prefix="/ai-test",
    tags=["AI Test"]
)

gemini = GeminiService()


@router.get("")
async def test_ai(message: str):

    result = gemini.classify(message)

    return result.model_dump()
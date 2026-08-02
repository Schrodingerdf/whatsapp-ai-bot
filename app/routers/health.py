from fastapi import APIRouter

router = APIRouter(tags=["Health"])


@router.get("/")
def home():
    return {
        "status": "online",
        "project": "WhatsApp AI Bot",
        "version": "1.0.0"
    }


@router.get("/health")
def health():
    return {
        "status": "healthy"
    }
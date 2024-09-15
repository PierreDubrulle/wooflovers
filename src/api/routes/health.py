from fastapi import APIRouter

router = APIRouter()


@router.get("/", response_model=dict)
def health() -> dict:
    """
    Health check
    """

    return {"status": "ok"}

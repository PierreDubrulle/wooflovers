from fastapi import APIRouter

from src.api.routes import health

api_router = APIRouter()

api_router.include_router(health.router, tags=["health"], prefix="/health")

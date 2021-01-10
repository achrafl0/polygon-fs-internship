from fastapi import APIRouter
from app.api.v1.endpoints import performances

api_router = APIRouter()
api_router.include_router(performances.router)
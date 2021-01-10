from typing import Optional
from fastapi import FastAPI
from app.middleware.RequestPerformanceMiddleWare import RequestPerformanceMiddleware
from app.db.init_db import engine, Base
from app.api.v1.router import api_router
from app.core.settings import settings

Base.metadata.create_all(bind=engine)
server = FastAPI(
    title=settings.SERVER_NAME,
    openapi_url=settings.OPEN_API_ROUTE,
)
server.add_middleware(RequestPerformanceMiddleware)
server.include_router(api_router, prefix=settings.API_ROUTE_STRING)

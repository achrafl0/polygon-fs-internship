from starlette.middleware.base import BaseHTTPMiddleware
import datetime
from sqlalchemy.orm import Session
from fastapi import Depends, Response
from app.models.tracking import TrackingModel
from app.db.init_db import SessionLocal


class RequestPerformanceMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        response = Response("Internal server error", status_code=500)
        start_time = datetime.datetime.now()
        try:
            db = SessionLocal()
            # We assign the local session to the request so we can use it as a dependency later on
            request.state.db = db
            response = await call_next(request)
            response_time = datetime.datetime.now()
            new_tracking = TrackingModel(
                request_time=start_time, response_time=response_time
            )
            db.add(new_tracking)
            db.commit()
            db.refresh(new_tracking)
        finally:
            request.state.db.close()
        return response
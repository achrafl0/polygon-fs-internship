from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import Dict
from app.core.dependencies import get_db
from app.schema.tracking import PerformanceBase
from app.api.v1.controllers import performancesControllers
from app.core.settings import settings

router = APIRouter()


@router.get("/performances", response_model=Dict[str, PerformanceBase])
def get_performances(db: Session = Depends(get_db)):
    """
    Returns stats about response time performance
    """
    response = {}
    for delay, delta in settings.PERFORMANCE_DELAYS.items():
        response[delay] = performancesControllers.get_trackings_since(db, delta)
    return response

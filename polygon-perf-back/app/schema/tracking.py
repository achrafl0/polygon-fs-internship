from typing import Optional
from pydantic import BaseModel
import datetime


class TrackingBase(BaseModel):
    id: int
    request_time: datetime.datetime
    response_time: datetime.timedelta


class TrackingCreate(TrackingBase):
    pass


class PerformanceBase(BaseModel):
    min_resp: float
    max_resp: float
    avg_resp: float

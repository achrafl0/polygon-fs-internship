from app.models.tracking import TrackingModel
from app.schema.tracking import PerformanceBase
from sqlalchemy.orm import Session
from sqlalchemy import func, text
import datetime


def get_trackings(db: Session, skip: int = 0, limit: int = 100):
    return db.query(TrackingModel).offset(skip).limit(limit).all()


def get_trackings_since(db: Session, since: datetime.timedelta):
    time_filter = datetime.datetime.now() - since
    trackings = (
        db.query(TrackingModel).filter(TrackingModel.request_time >= time_filter).all()
    )
    minresp = float("inf")
    maxresp = 0
    avgresp = 0
    if trackings:
        # We'll need to replace the follow by a more elaborate sql query to reduce overhead
        for track in trackings:
            delta = track.response_time - track.request_time
            delta = delta.total_seconds() * 1000
            minresp = min(delta, minresp)
            maxresp = max(delta, maxresp)
            avgresp += delta

        return PerformanceBase(
            min_resp=minresp, max_resp=maxresp, avg_resp=avgresp / len(trackings)
        )
    return PerformanceBase(min_resp=0.0, max_resp=0.0, avg_resp=0.0)

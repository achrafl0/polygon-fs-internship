from app.db.init_db import Base
from sqlalchemy import Column
from sqlalchemy.dialects.mysql import DATETIME, INTEGER


class TrackingModel(Base):
    __tablename__ = "trackings"
    id = Column(INTEGER, primary_key=True, index=True)
    # We need fractional second precision to the millisecond  as some of those queries are extremly fast
    request_time = Column(DATETIME(fsp=6))
    response_time = Column(DATETIME(fsp=6))

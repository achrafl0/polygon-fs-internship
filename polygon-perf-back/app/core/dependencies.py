from app.db.init_db import SessionLocal
from fastapi import Request


def get_db(request: Request):
    return request.state.db
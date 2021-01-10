from typing import Dict, List
from datetime import timedelta
from pydantic import BaseSettings


class Settings(BaseSettings):
    API_ROUTE_STRING: str = "/api/v1"
    SERVER_NAME: str = "Polygon Performance Backend"
    PERFORMANCE_DELAYS: Dict[str, timedelta] = {
        "24hours": timedelta(hours=24),
        "7days": timedelta(days=7),
        "28days": timedelta(days=28),
    }
    OPEN_API_ROUTE: str = "{}/doc/openapi.json".format(API_ROUTE_STRING)
    # We should change this to use .ENV variables , it's not secure like this
    MYSQL_URI: str = "mysql://polygon:polygon@polygon-perf-db:3306/db"
    ALLOWED_ORIGINS: List[str] = [
        "http://localhost",
        "http://localhost:8080",
        "polygon-perf-front",
    ]


settings = Settings()
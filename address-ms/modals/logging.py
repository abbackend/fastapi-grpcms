from datetime import datetime
from sqlalchemy import JSON, Column, Integer, String, DateTime
from core.database import Base

class Log(Base):
    __tablename__ = "logs"

    id = Column(Integer, primary_key=True)
    server = Column(String(10))
    level = Column(String(20))
    message = Column(String(255))
    extra = Column(JSON, default=[])
    created_at = Column(DateTime, default=datetime.now())

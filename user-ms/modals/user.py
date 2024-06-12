from sqlalchemy import Boolean, Column, Integer, String
from core.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String(100), unique=True, index=True)
    password = Column(String(255))
    is_active = Column(Boolean, default=True)

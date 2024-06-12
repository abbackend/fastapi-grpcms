from sqlalchemy import Boolean, Column, Integer, String, BigInteger
from core.database import Base

class Address(Base):
    __tablename__ = "addresses"

    id = Column(Integer, primary_key=True)
    street = Column(String(150))
    city = Column(String(10))
    state = Column(String(2))
    zip = Column(BigInteger)
    user_id = Column(Integer)
    is_default = Column(Boolean, default=False)

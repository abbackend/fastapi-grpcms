from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from core.config import settings

SQLALCHEMY_DATABASE_URL = "{}://{}:{}@{}/{}".format(
    settings.db_providor,
    settings.db_user,
    settings.db_pass,
    settings.db_host,
    settings.db_name,
)

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        return db
    finally:
        db.close()

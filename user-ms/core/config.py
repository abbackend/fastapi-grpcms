from pydantic_settings import BaseSettings
import logging


class Settings(BaseSettings):
    app_name: str = "USER-MS"
    logging_level: str = logging.getLevelName(logging.INFO)
    logging_format: str = ""
    port: int = 50051
    db_providor: str = "mysql"
    db_user: str = "root"
    db_pass: str = "root"
    db_name: str = "app"
    db_host: str = "db"
    jwt_secret: str = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
    jwt_algorithm: str = "HS256"
    jwt_expire: int = 30  # In minutes


settings = Settings()

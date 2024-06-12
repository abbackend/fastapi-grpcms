from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    jwt_secret: str = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
    jwt_algorithm: str = "HS256"
    jwt_expire: int = 30  # In minutes


settings = Settings()

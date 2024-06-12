from typing import Optional
from fastapi import HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from starlette.requests import Request
from core.config import settings
import jwt
from jwt.exceptions import InvalidTokenError


class JWTBearer(OAuth2PasswordBearer):
    def __init__(self):
        global jwt_token
        jwt_token = None
        super().__init__(tokenUrl="/auth/login")

    async def __call__(self, request: Request):
        token = await super().__call__(request)
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

        if not self.verify_jwt(token):
            raise credentials_exception

        global jwt_token
        jwt_token = token
        return jwt_token

    def verify_jwt(self, token: str) -> bool:
        try:
            payload = jwt.decode(
                token, settings.jwt_secret, algorithms=[settings.jwt_algorithm]
            )

            user_id: int = payload.get("sub")
            if user_id is None:
                return False

            return True
        except InvalidTokenError:
            return False

    def _get_token() -> Optional[str]:
        if jwt_token:
            return jwt_token

        return None

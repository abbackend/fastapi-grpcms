from fastapi import APIRouter, Depends
from clients.user import UserClient
from core.helpers.jwt_helper import JWTBearer

router = APIRouter(tags=["User"])
client = UserClient()


@router.get("/me")
async def get_active_user(d=Depends(JWTBearer())):
    return client.me()

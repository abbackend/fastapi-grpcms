from fastapi import APIRouter, Depends
from clients.address import AddressClient
from core.helpers.jwt_helper import JWTBearer
from schema.address import AddRequest

router = APIRouter(tags=["Address"])
client = AddressClient()


@router.post("")
async def add_address(request: AddRequest, d=Depends(JWTBearer())):
    return client.add(request)

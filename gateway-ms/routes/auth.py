from fastapi import APIRouter, Depends, HTTPException, status
from clients.auth import AuthClient
from schema.auth import LoginRequest, RegisterRequest, Token
from typing import Annotated
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(tags=["Auth"])
client = AuthClient()


@router.post("/login")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    request = LoginRequest(email=form_data.username, password=form_data.password)
    response = client.login(request)
    if "error" in response:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=response["error"],
            headers={"WWW-Authenticate": "Bearer"},
        )
    return Token(access_token=response["token"], token_type=response["token_type"])


@router.post("/register")
async def login(request: RegisterRequest):
    return client.register(request)

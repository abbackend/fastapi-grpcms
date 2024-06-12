from pydantic import BaseModel, EmailStr, Field


class LoginRequest(BaseModel):
    email: EmailStr
    password: str = Field(min_length=3)

class RegisterRequest(BaseModel):
    email: EmailStr
    password: str = Field(min_length=3)

class Token(BaseModel):
    access_token: str
    token_type: str

class AuthUser(BaseModel):
    user_id: int
    token: str
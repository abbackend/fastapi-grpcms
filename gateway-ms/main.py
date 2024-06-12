from fastapi import FastAPI
from routes.auth import router as auth_router
from routes.user import router as user_router
from routes.address import router as address_router

app = FastAPI(debug=True)
app.include_router(auth_router, prefix="/auth")
app.include_router(user_router, prefix="/user")
app.include_router(address_router, prefix="/address")

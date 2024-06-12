import logging
from grpc import StatusCode
from grpc_interceptor.exceptions import Unauthenticated, AlreadyExists
from sqlalchemy.orm import Session
from modals.user import User
from core.helpers.utils import verify_password, create_access_token, get_password_hash

from protos.auth.auth_pb2 import AuthLoginResponse, AuthRegisterResponse
from protos.auth.auth_pb2_grpc import AuthServicer


class AuthBaseService(AuthServicer):
    def __init__(self, db: Session):
        self.db = db

    def Login(self, request, context) -> AuthLoginResponse:
        logging.info("Called using the email %s", request.email)
        user = self.db.query(User).where(User.email == request.email).first()
        if user is None:
            raise Unauthenticated(
                details="Invalid email address!",
                status_code=StatusCode.UNAUTHENTICATED,
            )

        if not verify_password(request.password, user.password):
            raise Unauthenticated(
                details="Invalid Credentials!",
                status_code=StatusCode.UNAUTHENTICATED,
            )

        access_token = create_access_token(data={"sub": user.id})
        return AuthLoginResponse(
            user_id=user.id, token=access_token, token_type="bearer"
        )

    def Register(self, request, context) -> AuthRegisterResponse:
        user = self.db.query(User).where(User.email == request.email).first()
        if user is not None:
            raise AlreadyExists(
                details="Email address already exists!",
                status_code=StatusCode.ALREADY_EXISTS,
            )

        user = User(email=request.email, password=get_password_hash(request.password))
        self.db.add(user)
        self.db.commit()
        return AuthRegisterResponse(message="Registration successful!")

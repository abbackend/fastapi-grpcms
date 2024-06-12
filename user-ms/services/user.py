from grpc import StatusCode
from grpc_interceptor.exceptions import NotFound
from sqlalchemy.orm import Session
from modals.user import User
from core.helpers.jwt_interceptor import JwtInterceptor
from clients.address import AddressClient

from protos.user.user_pb2 import UserResponse
from protos.user.user_pb2_grpc import UserServicer


class UserBaseService(UserServicer):
    def __init__(self, db: Session):
        self.db = db
        self.address_client = AddressClient()

    def ActiveUser(self, request, context) -> UserResponse:
        user_id: int = JwtInterceptor._get_loggedin_id()
        user = self.db.query(User).where(User.id == user_id).first().man()
        if user is None:
            raise NotFound(
                details="User not fount!",
                status_code=StatusCode.NOT_FOUND,
            )

        addresses = self.address_client.get()
        return UserResponse(
            user_id=user.id,
            email=user.email,
            is_active=user.is_active,
            addresses=addresses["addresses"] if addresses else [],
        )

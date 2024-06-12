import logging
from grpc_interceptor.exceptions import NotFound
from sqlalchemy.orm import Session
from modals.address import Address
from core.helpers.jwt_interceptor import JwtInterceptor

from protos.address.address_pb2 import AddResponse, GetResponse
from protos.address.address_pb2_grpc import AddressServicer


class AddressBaseService(AddressServicer):
    def __init__(self, db: Session):
        self.db = db

    def Add(self, request, context) -> AddResponse:
        user_id: int = JwtInterceptor._get_loggedin_id()
        logging.info("Adding address for user %s", user_id)
        address = Address(
            street=request.street,
            city=request.city,
            state=request.state,
            zip=request.zip,
            is_default=False,
            user_id=user_id,
        )

        self.db.add(address)
        self.db.commit()

        return AddResponse(message="Added successfully!")

    def Get(self, request, context) -> GetResponse:
        user_id: int = JwtInterceptor._get_loggedin_id()
        addresses = []
        for address in self.db.query(Address).where(Address.user_id == user_id).all():
            addresses.append(
                {
                    "street": address.street,
                    "city": address.city,
                    "state": address.state,
                    "zip": address.zip,
                    "is_default": address.is_default,
                }
            )

        return GetResponse(addresses=addresses)

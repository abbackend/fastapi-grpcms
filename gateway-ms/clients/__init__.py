from core.helpers.jwt_helper import JWTBearer
from core.helpers.header_manipulator_interceptor import header_adder_interceptor
from protos.user.user_pb2_grpc import UserStub
from protos.auth.auth_pb2_grpc import AuthStub
from protos.address.address_pb2_grpc import AddressStub
import grpc


def get_auth_client_stub() -> AuthStub:
    channel = grpc.insecure_channel("user:50051")
    return AuthStub(channel)


def get_user_client_stub() -> UserStub:
    channel = grpc.insecure_channel("user:50051")
    interceptor = header_adder_interceptor("authorization", JWTBearer._get_token())
    intercept_channel = grpc.intercept_channel(channel, interceptor)
    return UserStub(intercept_channel)


def get_address_client_stub() -> AddressStub:
    channel = grpc.insecure_channel("address:50052")
    interceptor = header_adder_interceptor("authorization", JWTBearer._get_token())
    intercept_channel = grpc.intercept_channel(channel, interceptor)
    return AddressStub(intercept_channel)

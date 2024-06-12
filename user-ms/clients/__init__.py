from core.helpers.jwt_interceptor import JwtInterceptor
from core.helpers.header_manipulator_interceptor import header_adder_interceptor
from protos.address.address_pb2_grpc import AddressStub
import grpc


def get_address_client_stub() -> AddressStub:
    channel = grpc.insecure_channel("address:50052")
    interceptor = header_adder_interceptor(
        "authorization", JwtInterceptor._get_loggedin_token()
    )
    intercept_channel = grpc.intercept_channel(channel, interceptor)
    return AddressStub(intercept_channel)

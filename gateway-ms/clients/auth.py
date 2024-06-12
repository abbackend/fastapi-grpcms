import grpc
from core.helpers.grpc_error_code_mapper import generate_exception
from google.protobuf.json_format import MessageToDict
from schema.auth import LoginRequest, RegisterRequest
from clients import get_auth_client_stub

from protos.auth.auth_pb2 import AuthLoginRequest, AuthRegisterRequest


class AuthClient(object):
    def login(self, request: LoginRequest):
        try:
            response = get_auth_client_stub().Login(
                AuthLoginRequest(email=request.email, password=request.password)
            )
            return MessageToDict(
                response,
                preserving_proto_field_name=True,
            )
        except grpc.RpcError as rpc_error:
            return {"error": rpc_error.details()}

    def register(self, request: RegisterRequest):
        try:
            response = get_auth_client_stub().Register(
                AuthRegisterRequest(email=request.email, password=request.password)
            )
            return MessageToDict(
                response,
                preserving_proto_field_name=True,
            )
        except grpc.RpcError as rpc_error:
            raise generate_exception(rpc_error)

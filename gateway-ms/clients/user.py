import grpc
from google.protobuf.json_format import MessageToDict
from clients import get_user_client_stub

from protos.user.user_pb2 import UserRequest
from core.helpers.grpc_error_code_mapper import generate_exception


class UserClient(object):
    def me(self):
        try:
            response = get_user_client_stub().ActiveUser(UserRequest())
            return MessageToDict(
                response,
                preserving_proto_field_name=True,
            )
        except grpc.RpcError as rpc_error:
            raise generate_exception(rpc_error)

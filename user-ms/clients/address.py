from fastapi import HTTPException
import grpc
from google.protobuf.json_format import MessageToDict
from clients import get_address_client_stub

from protos.address.address_pb2 import GetRequest


class AddressClient(object):
    def get(self):
        try:
            response = get_address_client_stub().Get(GetRequest())
            return MessageToDict(
                response,
                preserving_proto_field_name=True,
            )
        except grpc.RpcError as rpc_error:
            raise HTTPException(
                detail=rpc_error.details(), status_code=rpc_error.status_code
            )

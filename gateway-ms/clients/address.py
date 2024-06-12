from fastapi import HTTPException
import grpc
from google.protobuf.json_format import MessageToDict
from schema.address import AddRequest
from clients import get_address_client_stub
from core.helpers.grpc_error_code_mapper import generate_exception

from protos.address.address_pb2 import AddRequest as AddAddressRequest


class AddressClient(object):
    def add(self, request: AddRequest):
        try:
            response = get_address_client_stub().Add(
                AddAddressRequest(
                    street=request.street,
                    city=request.city,
                    state=request.state,
                    zip=request.zip,
                )
            )
            return MessageToDict(
                response,
                preserving_proto_field_name=True,
            )
        except grpc.RpcError as rpc_error:
            raise generate_exception(rpc_error)

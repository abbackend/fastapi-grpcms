from concurrent import futures
from core.helpers.logging import setup

import grpc, logging
from grpc_interceptor import ExceptionToStatusInterceptor

from core.config import settings
from protos.address.address_pb2_grpc import add_AddressServicer_to_server
from services.address import AddressBaseService
from core.database import engine, Base, get_db
from core.helpers.jwt_interceptor import JwtInterceptor

Base.metadata.create_all(bind=engine, checkfirst=True)
db = get_db()


def serve():
    interceptors = [
        ExceptionToStatusInterceptor(),
        JwtInterceptor(grpc.StatusCode.UNAUTHENTICATED, "Access denied!"),
    ]
    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=10), interceptors=interceptors
    )
    add_AddressServicer_to_server(AddressBaseService(db), server)
    server.add_insecure_port("[::]:{}".format(settings.port))
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    setup()
    logging.info("Address Server Starter...")
    serve()

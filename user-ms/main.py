from concurrent import futures

import grpc, logging
from grpc_interceptor import ExceptionToStatusInterceptor

from core.config import settings
from protos.auth.auth_pb2_grpc import add_AuthServicer_to_server
from protos.user.user_pb2_grpc import add_UserServicer_to_server
from services.auth import AuthBaseService
from services.user import UserBaseService
from core.database import engine, Base, get_db
from core.helpers.jwt_interceptor import JwtInterceptor
from core.helpers.logging import setup

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
    add_AuthServicer_to_server(AuthBaseService(db), server)
    add_UserServicer_to_server(UserBaseService(db), server)
    server.add_insecure_port("[::]:{}".format(settings.port))
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    setup()
    logging.info("User Server Starter...")
    serve()

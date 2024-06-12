from grpc import StatusCode as Code, RpcError
from fastapi import status, HTTPException

StatusCode = {
    Code.OK: status.HTTP_200_OK,
    Code.NOT_FOUND: status.HTTP_404_NOT_FOUND,
    Code.ALREADY_EXISTS: status.HTTP_422_UNPROCESSABLE_ENTITY,
    Code.ABORTED: status.HTTP_422_UNPROCESSABLE_ENTITY,
    Code.PERMISSION_DENIED: status.HTTP_403_FORBIDDEN,
    Code.UNAUTHENTICATED: status.HTTP_401_UNAUTHORIZED,
}


def generate_exception(error: RpcError):
    code = (
        StatusCode[error.code()]
        if error.code() in StatusCode
        else status.HTTP_500_INTERNAL_SERVER_ERROR
    )

    return HTTPException(detail=error.details(), status_code=code)

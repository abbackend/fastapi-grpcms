import grpc, jwt
from typing import Optional
from jwt.exceptions import InvalidTokenError
from core.config import settings

excluded_targets = ["/auth.Auth/Login", "/auth.Auth/Register"]


def _unary_unary_rpc_terminator(code, details):
    def terminate(ignored_request, context):
        context.abort(code, details)

    return grpc.unary_unary_rpc_method_handler(terminate)


class JwtInterceptor(grpc.ServerInterceptor):
    def __init__(self, code, details):
        global logged_in_id
        global logged_in_token
        logged_in_id = None
        logged_in_token = None
        self._terminator = _unary_unary_rpc_terminator(code, details)

    def intercept_service(self, continuation, handler_call_details):
        jwt_token = ""
        for header, value in handler_call_details.invocation_metadata:
            if header.lower() == "authorization":
                jwt_token = value

        if handler_call_details.method in excluded_targets:
            return continuation(handler_call_details)

        if not jwt_token or not self.verify_jwt(jwt_token):
            return self._terminator

        return continuation(handler_call_details)

    def verify_jwt(self, token: str) -> bool:
        try:
            payload = jwt.decode(
                token, settings.jwt_secret, algorithms=[settings.jwt_algorithm]
            )

            user_id: int = payload.get("sub")
            if user_id is None:
                return False

            global logged_in_id
            global logged_in_token
            logged_in_id = user_id
            logged_in_token = token
            return True
        except InvalidTokenError:
            return False

    def _get_loggedin_id() -> Optional[int]:
        if logged_in_id:
            return logged_in_id

        return None

    def _get_loggedin_token() -> Optional[str]:
        if logged_in_token:
            return logged_in_token

        return None
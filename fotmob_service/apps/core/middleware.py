"""Core middleware."""
import uuid
import structlog

logger = structlog.get_logger(__name__)


class RequestIDMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.request_id = str(uuid.uuid4())
        response = self.get_response(request)
        response["X-Request-ID"] = request.request_id
        return response


class StructuredLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        structlog.contextvars.clear_contextvars()
        structlog.contextvars.bind_contextvars(
            request_id=getattr(request, "request_id", "-"),
            method=request.method,
            path=request.path,
        )
        response = self.get_response(request)
        logger.info("request_finished", status=response.status_code)
        return response

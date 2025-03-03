# backend/app/core/rate_limiter.py
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response
import time

class RateLimiterMiddleware(BaseHTTPMiddleware):
    """
    A simple in-memory rate limiting middleware.
    Note: For production, consider using a distributed store like Redis.
    """
    RATE_LIMIT = 100  # Maximum requests per time window
    TIME_WINDOW = 60  # Time window in seconds

    def __init__(self, app):
        super().__init__(app)
        self.clients = {}

    async def dispatch(self, request: Request, call_next):
        client_ip = request.client.host
        now = time.time()

        # Initialize or reset the record for the client
        record = self.clients.get(client_ip, {"count": 0, "start_time": now})
        if now - record["start_time"] > self.TIME_WINDOW:
            record = {"count": 0, "start_time": now}

        record["count"] += 1
        self.clients[client_ip] = record

        if record["count"] > self.RATE_LIMIT:
            return Response("Rate limit exceeded", status_code=429)

        response = await call_next(request)
        return response

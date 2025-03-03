# backend/app/core/errors.py
from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse

def add_exception_handlers(app):
    """
    Add custom exception handlers to the FastAPI app.
    """
    @app.exception_handler(HTTPException)
    async def http_exception_handler(request: Request, exc: HTTPException):
        return JSONResponse(
            status_code=exc.status_code,
            content={"detail": exc.detail},
        )

    @app.exception_handler(Exception)
    async def generic_exception_handler(request: Request, exc: Exception):
        # In production, log the error details for debugging.
        return JSONResponse(
            status_code=500,
            content={"detail": "Internal Server Error"},
        )

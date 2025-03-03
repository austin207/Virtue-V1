# backend/app/main.py
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import routers from our API endpoints
from app.api.routes import chat, auth, admin
# Import custom exception handlers and middleware
from app.core.errors import add_exception_handlers
from app.core.rate_limiter import RateLimiterMiddleware
# Import database engine and Base for creating tables
from app.db.database import engine, Base

# Create FastAPI app instance
app = FastAPI(title="LLM Chat App API", version="1.0.0")

# Enable CORS middleware (adjust allowed origins as needed for production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify the exact origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add custom rate limiting middleware
app.add_middleware(RateLimiterMiddleware)

# Include API routers for authentication, chat, and admin
app.include_router(auth.router, prefix="/api/auth", tags=["Authentication"])
app.include_router(chat.router, prefix="/api/chat", tags=["Chat"])
app.include_router(admin.router, prefix="/api/admin", tags=["Admin"])

# Add custom exception handlers
add_exception_handlers(app)

# Create database tables (for production, use Alembic migrations)
Base.metadata.create_all(bind=engine)

# Uvicorn entry point
if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)

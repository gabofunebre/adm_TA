from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware

from app.api.routers import auth, registration, pages
from app.database import Base, engine, SessionLocal
from app.services.logging_middleware import LoggingMiddleware
import app.models
from app.core.security import get_password_hash
from app.core.config import get_settings

settings = get_settings()

Base.metadata.create_all(bind=engine)

# Ensure a default admin user exists for initial access
with SessionLocal() as db:
    admin = db.query(app.models.User).filter(
        app.models.User.username == settings.ADMIN_USERNAME
    ).first()
    if not admin:
        admin_user = app.models.User(
            username=settings.ADMIN_USERNAME,
            hashed_password=get_password_hash(settings.ADMIN_PASSWORD),
            first_name="Admin",
            last_name="User",
            email=settings.ADMIN_EMAIL,
        )
        db.add(admin_user)
        db.commit()

app = FastAPI(title="adm_TA")


@app.get("/", include_in_schema=False)
def root() -> RedirectResponse:
    """Redirect base path to interactive API docs."""
    return RedirectResponse("/docs")


app.add_middleware(LoggingMiddleware)
app.add_middleware(SessionMiddleware, secret_key=settings.JWT_SECRET_KEY)

app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.include_router(auth.router)
app.include_router(registration.router)
app.include_router(pages.router)

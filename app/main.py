from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.api.routers import auth, users, accounts, movements, dashboard, registration, orders
from app.database import Base, engine, SessionLocal
from app.services.logging_middleware import LoggingMiddleware
from pathlib import Path
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

app = FastAPI(title="Movimientos de Dinero")

app.add_middleware(LoggingMiddleware)


app.include_router(auth.router)
app.include_router(users.router)
app.include_router(accounts.router)
app.include_router(movements.router)
app.include_router(dashboard.router)
app.include_router(registration.router)
app.include_router(orders.router)
app.mount(
    "/",
    StaticFiles(directory=Path(__file__).parent.parent / "frontend" / "dist", html=True),
    name="frontend",
)

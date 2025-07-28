from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.api.routers import auth, users, accounts, movements, dashboard, registration
from app.database import Base, engine
from app.services.logging_middleware import LoggingMiddleware
from pathlib import Path

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Movimientos de Dinero")

app.add_middleware(LoggingMiddleware)


app.mount(
    "/",
    StaticFiles(directory=Path(__file__).parent.parent / "frontend" / "dist", html=True),
    name="frontend"
)
app.include_router(auth.router)
app.include_router(users.router)
app.include_router(accounts.router)
app.include_router(movements.router)
app.include_router(dashboard.router)
app.include_router(registration.router)

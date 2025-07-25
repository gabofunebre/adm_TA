from fastapi import FastAPI

from app.api.routers import auth, users, accounts, movements, dashboard
from app.database import Base, engine
from app.services.logging_middleware import LoggingMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Movimientos de Dinero")

app.add_middleware(LoggingMiddleware)


@app.get("/")
def read_root():
    """Basic index route for health checks."""
    return {"message": "Welcome to Movimientos de Dinero API"}

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(accounts.router)
app.include_router(movements.router)
app.include_router(dashboard.router)

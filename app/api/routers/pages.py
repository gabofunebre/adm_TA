from fastapi import APIRouter, Request, Depends, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.database import get_db
from app.api.dependencies import authenticate_user
from app.core.security import get_password_hash
from app import models

router = APIRouter(tags=["pages"])

templates = Jinja2Templates(directory="app/templates")


@router.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@router.post("/login")
async def login(
    request: Request,
    username: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db),
):
    user = authenticate_user(db, username, password)
    if not user:
        return templates.TemplateResponse(
            "login.html",
            {"request": request, "error": "Credenciales inválidas"},
            status_code=400,
        )
    request.session["user_id"] = user.id
    request.session["user_name"] = user.first_name or user.username
    return RedirectResponse(url="/welcome", status_code=303)


@router.get("/register", response_class=HTMLResponse)
async def register_page(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})


@router.post("/register")
async def register(
    request: Request,
    first_name: str = Form(...),
    last_name: str = Form(...),
    email: str = Form(...),
    password: str = Form(...),
    confirm_password: str = Form(...),
    db: Session = Depends(get_db),
):
    if password != confirm_password:
        return templates.TemplateResponse(
            "register.html",
            {"request": request, "error": "Las contraseñas no coinciden"},
            status_code=400,
        )
    existing = db.query(models.User).filter(models.User.username == email).first()
    if existing:
        return templates.TemplateResponse(
            "register.html",
            {"request": request, "error": "El usuario ya existe"},
            status_code=400,
        )
    user = models.User(
        username=email,
        email=email,
        first_name=first_name,
        last_name=last_name,
        hashed_password=get_password_hash(password),
    )
    db.add(user)
    db.commit()
    return RedirectResponse(url="/login", status_code=303)


@router.get("/welcome", response_class=HTMLResponse)
async def welcome(request: Request):
    user_id = request.session.get("user_id")
    if not user_id:
        return RedirectResponse(url="/login", status_code=303)
    user_name = request.session.get("user_name", "Usuario")
    return templates.TemplateResponse(
        "welcome.html", {"request": request, "user_name": user_name}
    )


@router.post("/logout")
async def logout(request: Request):
    request.session.clear()
    return RedirectResponse(url="/login", status_code=303)

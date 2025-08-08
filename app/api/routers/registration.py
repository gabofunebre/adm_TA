from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import uuid4

from app.database import get_db
from app import models
from app.schemas.registration import RegistrationCreate, RegistrationRead
from app.core.security import get_password_hash
from app.core.config import get_settings
from app.services.mailer import send_email

router = APIRouter(prefix="/registrations", tags=["registrations"])
settings = get_settings()


@router.post('/', response_model=RegistrationRead)
def create_registration(reg_in: RegistrationCreate, db: Session = Depends(get_db)):
    reg = models.Registration(
        first_name=reg_in.first_name,
        last_name=reg_in.last_name,
        email=reg_in.email,
        hashed_password=get_password_hash(reg_in.password),
        admin_token=str(uuid4()),
        user_token=str(uuid4()),
    )
    db.add(reg)
    db.commit()
    db.refresh(reg)

    approve_link = f"{settings.BASE_URL}/registrations/{reg.id}/approve?token={reg.admin_token}"
    reject_link = f"{settings.BASE_URL}/registrations/{reg.id}/reject?token={reg.admin_token}"
    body = (
        f"<p>Nuevo registro de {reg.first_name} {reg.last_name} ({reg.email}).</p>"
        f"<p><a href='{approve_link}'>Aprobar</a> | <a href='{reject_link}'>Rechazar</a></p>"
    )
    send_email(settings.ADMIN_EMAIL, "Nuevo registro", body)
    return reg


@router.get('/{reg_id}/approve')
def approve_registration(reg_id: int, token: str, db: Session = Depends(get_db)):
    reg = db.query(models.Registration).filter(models.Registration.id == reg_id).first()
    if not reg or reg.admin_token != token or reg.rejected:
        raise HTTPException(status_code=404, detail="Invalid registration")
    reg.approved = True
    db.commit()
    confirm_link = f"{settings.BASE_URL}/registrations/{reg.id}/confirm?token={reg.user_token}"
    body = (
        f"<p>Su registro fue aprobado.</p>"
        f"<p><a href='{confirm_link}'>Confirmar cuenta</a></p>"
    )
    send_email(reg.email, "Registro aprobado", body)
    return {"ok": True}


@router.get('/{reg_id}/reject')
def reject_registration(reg_id: int, token: str, db: Session = Depends(get_db)):
    reg = db.query(models.Registration).filter(models.Registration.id == reg_id).first()
    if not reg or reg.admin_token != token or reg.approved:
        raise HTTPException(status_code=404, detail="Invalid registration")
    reg.rejected = True
    db.commit()
    send_email(reg.email, "Registro rechazado", "<p>Su registro fue rechazado.</p>")
    return {"ok": True}


@router.get('/{reg_id}/confirm')
def confirm_registration(reg_id: int, token: str, db: Session = Depends(get_db)):
    reg = db.query(models.Registration).filter(models.Registration.id == reg_id).first()
    if not reg or reg.user_token != token or not reg.approved or reg.rejected:
        raise HTTPException(status_code=404, detail="Invalid registration")
    if reg.confirmed:
        return {"detail": "Already confirmed"}
    user = models.User(
        username=reg.email,
        email=reg.email,
        first_name=reg.first_name,
        last_name=reg.last_name,
        hashed_password=reg.hashed_password,
    )
    db.add(user)
    reg.confirmed = True
    db.commit()
    send_email(reg.email, "Cuenta creada", "<p>Su cuenta ha sido creada.</p>")
    return {"ok": True}

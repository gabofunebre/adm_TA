from datetime import date
from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app import models
from app.api.dependencies import get_current_user
from app.database import get_db
from app.schemas.movement import MovementCreate, MovementRead

router = APIRouter(prefix="/movements", tags=["movements"])


def create_transfer(db: Session, movement: models.Movement, current_user: models.User):
    opposite_type = models.MovementType.income if movement.type == models.MovementType.expense else models.MovementType.expense
    transfer = models.Movement(
        date=movement.date,
        detail=f"Transferencia {movement.detail}",
        amount=movement.amount,
        type=opposite_type,
        account_id=movement.transfer_id,
        user_id=current_user.id,
        note=movement.note,
    )
    db.add(transfer)
    db.flush()
    movement.transfer_id = transfer.id


@router.post('/', response_model=MovementRead)
def create_movement(movement_in: MovementCreate, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    movement = models.Movement(**movement_in.dict(exclude_unset=True), user_id=current_user.id)
    db.add(movement)
    if movement.transfer_id:
        create_transfer(db, movement, current_user)
    db.commit()
    db.refresh(movement)
    return movement


@router.get('/', response_model=List[MovementRead])
def list_movements(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
    start_date: Optional[date] = Query(None),
    end_date: Optional[date] = Query(None),
    account_id: Optional[int] = Query(None),
    type: Optional[str] = Query(None)
):
    query = db.query(models.Movement).filter(models.Movement.user_id == current_user.id)
    if start_date:
        query = query.filter(models.Movement.date >= start_date)
    if end_date:
        query = query.filter(models.Movement.date <= end_date)
    if account_id:
        query = query.filter(models.Movement.account_id == account_id)
    if type:
        query = query.filter(models.Movement.type == models.MovementType(type))
    return query.all()

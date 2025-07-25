from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import models
from app.api.dependencies import get_current_user
from app.database import get_db

router = APIRouter(prefix="/dashboard", tags=["dashboard"])


def get_account_balance(db: Session, account: models.Account) -> float:
    income = db.query(models.Movement).filter(models.Movement.account_id == account.id, models.Movement.type == models.MovementType.income).with_entities(models.Movement.amount)
    expense = db.query(models.Movement).filter(models.Movement.account_id == account.id, models.Movement.type == models.MovementType.expense).with_entities(models.Movement.amount)
    income_total = sum([i[0] for i in income]) if income else 0.0
    expense_total = sum([e[0] for e in expense]) if expense else 0.0
    return income_total - expense_total


@router.get('/')
def dashboard(db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    accounts = db.query(models.Account).filter(models.Account.user_id == current_user.id).all()
    total_general = 0.0
    totals_by_account = {}
    for account in accounts:
        balance = get_account_balance(db, account)
        totals_by_account[account.name] = balance
        total_general += balance
    return {
        "total": total_general,
        "by_account": totals_by_account
    }

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import models
from app.api.dependencies import get_current_user
from app.database import get_db
from app.schemas.account import AccountCreate, AccountRead

router = APIRouter(prefix="/accounts", tags=["accounts"])


@router.post('/', response_model=AccountRead)
def create_account(account_in: AccountCreate, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    account = models.Account(name=account_in.name, currency=account_in.currency, user_id=current_user.id)
    db.add(account)
    db.commit()
    db.refresh(account)
    return account


def get_balance(account: models.Account) -> float:
    income = sum(m.amount for m in account.movements if m.type == models.MovementType.income)
    expense = sum(m.amount for m in account.movements if m.type == models.MovementType.expense)
    return income - expense


@router.get('/', response_model=list[AccountRead])
def list_accounts(db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    accounts = db.query(models.Account).filter(models.Account.user_id == current_user.id).all()
    result = []
    for acc in accounts:
        balance = get_balance(acc)
        result.append(AccountRead.from_orm(acc).copy(update={"balance": balance}))
    return result


@router.delete('/{account_id}')
def delete_account(account_id: int, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    account = db.query(models.Account).filter(models.Account.id == account_id, models.Account.user_id == current_user.id).first()
    if not account:
        raise HTTPException(status_code=404, detail="Account not found")
    db.delete(account)
    db.commit()
    return {"ok": True}

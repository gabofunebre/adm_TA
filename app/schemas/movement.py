from datetime import date
from typing import Optional
from pydantic import BaseModel

class MovementBase(BaseModel):
    date: date
    detail: str
    amount: float
    type: str
    account_id: int
    note: Optional[str] = None
    transfer_id: Optional[int] = None

class MovementCreate(MovementBase):
    pass

class MovementRead(MovementBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True

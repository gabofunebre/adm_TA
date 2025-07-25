from pydantic import BaseModel
from typing import Optional

class AccountCreate(BaseModel):
    name: str
    currency: str

class AccountRead(BaseModel):
    id: int
    name: str
    currency: str
    balance: Optional[float] = 0.0

    class Config:
        orm_mode = True

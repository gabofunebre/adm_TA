from datetime import date
from typing import Optional
from pydantic import BaseModel


class OrderBase(BaseModel):
    date: Optional[date] = None
    client: str
    phone: str
    address: str
    photo: Optional[str] = None
    total: Optional[float] = None
    deposit: Optional[float] = None
    depositRef: Optional[str] = None
    preBalance: Optional[float] = None
    balance: Optional[float] = None
    seller: Optional[str] = None
    installer: Optional[str] = None
    installDate: Optional[date] = None
    notes: Optional[str] = None
    status: str


class OrderCreate(OrderBase):
    pass


class OrderRead(OrderBase):
    id: int

    class Config:
        orm_mode = True

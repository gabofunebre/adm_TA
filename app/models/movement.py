from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey, Enum
from sqlalchemy.orm import relationship
import enum

from .base import Base

class MovementType(enum.Enum):
    income = 'income'
    expense = 'expense'

class Movement(Base):
    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, nullable=False)
    detail = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    type = Column(Enum(MovementType), nullable=False)
    account_id = Column(Integer, ForeignKey('account.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
    note = Column(String, nullable=True)
    transfer_id = Column(Integer, ForeignKey('movement.id'), nullable=True)

    user = relationship('User', back_populates='movements', foreign_keys=[user_id])
    account = relationship('Account', back_populates='movements')
    transfer = relationship('Movement', remote_side=[id])

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from .base import Base

class Account(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    currency = Column(String(3), nullable=False, default='ARS')
    user_id = Column(Integer, ForeignKey('user.id'))

    user = relationship('User', back_populates='accounts')
    movements = relationship('Movement', back_populates='account')

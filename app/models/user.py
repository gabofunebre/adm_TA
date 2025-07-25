from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from .base import Base

class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)

    movements = relationship('Movement', back_populates='user')
    accounts = relationship('Account', back_populates='user')

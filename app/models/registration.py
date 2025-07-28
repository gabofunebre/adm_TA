from sqlalchemy import Column, Integer, String, Boolean
from .base import Base

class Registration(Base):
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    admin_token = Column(String, unique=True, nullable=False)
    user_token = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    approved = Column(Boolean, default=False)
    rejected = Column(Boolean, default=False)
    confirmed = Column(Boolean, default=False)

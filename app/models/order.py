from sqlalchemy import Column, Integer, String, Date, Enum, Float
import enum

from .base import Base


class OrderStatus(enum.Enum):
    ingresado = 'ingresado'
    en_proceso = 'en_proceso'
    finalizado = 'finalizado'


class Order(Base):
    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, nullable=True)
    client = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    address = Column(String, nullable=False)
    photo = Column(String, nullable=True)
    total = Column(Float, nullable=True)
    deposit = Column(Float, nullable=True)
    depositRef = Column(String, nullable=True)
    preBalance = Column(Float, nullable=True)
    balance = Column(Float, nullable=True)
    seller = Column(String, nullable=True)
    installer = Column(String, nullable=True)
    installDate = Column(Date, nullable=True)
    notes = Column(String, nullable=True)
    status = Column(Enum(OrderStatus), nullable=False, default=OrderStatus.ingresado)

from sqlalchemy.orm import declared_attr
from sqlalchemy.ext.declarative import as_declarative

@as_declarative()
class Base:
    id: int

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

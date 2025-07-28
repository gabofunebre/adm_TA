from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    password: str | None = None
    first_name: str | None = None
    last_name: str | None = None
    email: str | None = None

class UserRead(BaseModel):
    id: int
    username: str
    first_name: str | None = None
    last_name: str | None = None
    email: str | None = None

    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    username: str
    password: str

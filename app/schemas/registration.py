from pydantic import BaseModel, EmailStr

class RegistrationCreate(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    password: str

class RegistrationRead(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: EmailStr
    approved: bool
    rejected: bool
    confirmed: bool

    class Config:
        orm_mode = True

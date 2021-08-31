from typing import List, Optional
from pydantic import Field, EmailStr, BaseModel


class UserRegiser(BaseModel):
    email: EmailStr
    username: str
    password: str = Field(min_length=8)


class UserLogin(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8)


class JwtUserData(BaseModel):
    id: int
    email: EmailStr
    username: str

#Python Core
from typing import Optional
from uuid import UUID
from datetime import date
from datetime import datetime


# Pydantic
from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import Field

# FastAPI
from fastapi import FastAPI

# Models

class UserBase(BaseModel):
    user_id: UUID = Field(...,)
    email: EmailStr = Field(...,)


class PasswordMixin(BaseModel):   # Creamos este nuevo modelo
    password: str = Field(
        ...,
        min_length=8,
        max_length=64,
        example='password',
        )


class User(UserBase):
    first_name: str = Field(
        ...,
        min_length=1,
        max_length=50
        )
    last_name: str = Field(
        ...,
        min_length=1,
        max_length=50
        )
    birth_date: Optional[date] = Field(default=None)


class UserLogin(PasswordMixin,UserBase):
    pass


class UserRegister(PasswordMixin, User):
    pass



class Tweet(BaseModel):
    tweet_id: UUID = Field(...)
    content: str = Field(
        ...,
        min_length=1,
        max_length=280
    )
    created_at: datetime = Field(default=datetime.now())
    updated_at: Optional[datetime] = Field(default=None)
    by: User = Field(...)
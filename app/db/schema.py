from typing import Any, List, Optional


import peewee

from pydantic import BaseModel
from pydantic.utils import GetterDict


class PeeweeGetDict(GetterDict):

    def get(self, key: Any, default: Any = None):

        res = getattr(self._obj, key, default)

        if isinstance(res, peewee.ModelSelect):

            return list(res)

        return res


class BlogBase(BaseModel):
    title: str
    created_date: str
    body: str


class BlogCreate(BlogBase):
    pass


class Blog(BlogBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetDict


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    blogs: List[Blog] = []

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetDict

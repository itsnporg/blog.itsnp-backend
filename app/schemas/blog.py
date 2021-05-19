from typing import Optional
from pydantic import BaseModel


class BlogBase(BaseModel):
    pass


class BlogCreate(BlogBase):
    pass


class BlogUpdate(BlogBase):
    pass


class BlogInDB(BlogBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True

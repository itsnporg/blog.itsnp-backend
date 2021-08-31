from collections import UserString
from typing import Dict, Union

from sqlalchemy.dialects.postgresql.array import Any
from app.db.session import SessionLocal
from app.db.crud.base import CRUDBase
from sqlalchemy.orm import Session
from app.db.models.user import User
from fastapi import HTTPException, status
from app.schemas.user import *


class UserCrud(CRUDBase[User, UserRegiser, UserRegiser]):
    def __init__(self):
        super().__init__(User)

    def get_user_by_email(self, db: Session, email: str) -> User:
        return db.query(self.model).filter(self.model.email == email).first()

    def create(self, db: Session, user: UserRegiser) -> User:
        if self.does_user_exists_with_email(db, user.email):
            raise HTTPException(status.HTTP_400_BAD_REQUEST, detail="User Already Exists with email")
        
        if self.does_user_exists_with_username(db, user.username):
            raise HTTPException(status.HTTP_400_BAD_REQUEST, detail="User Already Exists with username")
        
        db_user = User(email=user.email, username=user.username)
        db_user.set_password(user.password)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

    def remove(self, db: Session, id: int) -> User:
        raise NotImplementedError("This Method is not yet implemented for UserCrud")

    def update(
        self,
        db: Session,
        *,
        db_obj: User,
        obj_in: Union[User, Dict[str, Any]]
    ) -> User:
        raise NotImplementedError("This Method is not yet implemented for UserCrud")

    def does_user_exists_with_username(self, db: Session, username: str) -> bool:
        return bool(db.query(self.model).filter(self.model.username == username))

    def does_user_exists_with_email(self, db: Session, email: str) -> bool:
        return bool(db.query(self.model).filter(self.model.email == email))

user_crud = UserCrud()

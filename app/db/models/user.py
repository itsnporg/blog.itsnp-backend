import sqlalchemy as sa
from sqlalchemy.orm import defaultload
from sqlalchemy.sql.expression import null
from app.db.session import Base
from sqlalchemy.sql import func
from datetime import datetime
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_current_time():
    return datetime.now()


class User(Base):
    __tablename__ = "users"

    id = sa.Column(sa.Integer, primary_key=True, index=True, nullable=False)
    username = sa.Column(sa.String, index=True, unique=True, nullable=False)
    email = sa.Column(sa.String, index=True, unique=True, nullable=False)
    hashed_password = sa.Column(sa.String, nullable=False)
    creation_date = sa.Column(sa.DateTime, default=get_current_time, nullable=False)
    last_login = sa.Column(sa.DateTime, nullable=True)

    def set_password(self, password: str):
        self.hashed_password = pwd_context.hash(password)

    def check_password(self, password: str) -> bool:
        return pwd_context.verify(password, self.hashed_password)


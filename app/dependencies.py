from warnings import simplefilter
from fastapi.security.http import HTTPAuthorizationCredentials

from sqlalchemy.sql.expression import false
from app.schemas.user import JwtUserData
from app.db.models.user import User
from typing import Dict, Generator
from app.db.session import SessionLocal
from jose import JWTError, jwt
from fastapi import Depends, status, HTTPException
from fastapi.security import HTTPBearer
from datetime import datetime, timedelta
from app.core.config import settings



def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


jwtBearerAuth = HTTPBearer()

class AuthenticationManager:
    def __init__(self) -> None:
        self.user: JwtUserData
        self.token: str
        self.is_user_authenticated: bool = False

    def authenticate_user_with_token(self, token: str):
        self.token = token
        self.user = self.get_athenticated_user()
        self.is_user_authenticated = True

    @classmethod
    def only_authorized_user(cls, credentials: HTTPAuthorizationCredentials = Depends(jwtBearerAuth)) -> "AuthenticationManager":
        self = cls()
        self.authenticate_user_with_token(credentials.credentials)
        return self

    def get_athenticated_user(self) -> JwtUserData:
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        try:
            payload = jwt.decode(self.token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
            id: int = int(payload.get("id"))
            email: str = payload.get("email")
            username: str = payload.get("username")
            
            if username is None or email is None or id is None:
                raise credentials_exception
        except JWTError as e:
            raise credentials_exception
        user = JwtUserData(id=id, email=email, username=username)
        return user

    def create_access_token(self, user_data: JwtUserData) -> Dict[str, object]:
        data: Dict[str, object] = user_data.dict()
        expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        data.update({"exp": expire})
        encoded_jwt = jwt.encode(
            data, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
        return {"access_token": encoded_jwt, "token_type": "Bearer", "expires": expire}

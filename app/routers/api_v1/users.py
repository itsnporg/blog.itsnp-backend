from fastapi import APIRouter, HTTPException, status, Depends
from app.schemas.user import JwtUserData, UserLogin, UserRegiser
from jose import JWTError, jwt
from datetime import datetime, timedelta
from typing import Optional
from app.db.crud.user import UserCrud, user_crud
from app.dependencies import AuthenticationManager, get_db, SessionLocal
from app.core.config import settings

router = APIRouter()


@router.post("/regiser")
def register(user: UserRegiser, db: SessionLocal=Depends(get_db), authManager: AuthenticationManager=Depends(AuthenticationManager)):
    user = user_crud.create(db, user)
    user_data = JwtUserData(id=user.id, email=user.email, username=user.username)
    return authManager.create_access_token(user_data)


@router.post("/login")
def login(user: UserLogin, db: SessionLocal=Depends(get_db), authManager: AuthenticationManager=Depends(AuthenticationManager)):
    userInDb = user_crud.get_user_by_email(db, user.email)
    if userInDb is None or not userInDb.check_password(user.password):
        raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Crentials Provided were wrong",
            )
    
    user_data = JwtUserData(id=userInDb.id, email=userInDb.email, username=userInDb.username)
    return authManager.create_access_token(user_data)


@router.get("/current")
def get_current_user(authManager: AuthenticationManager=Depends(AuthenticationManager.only_authorized_user)):
    return authManager.user

from fastapi import APIRouter
from app.routers.api_v1 import blogs, users

router = APIRouter()

router.include_router(blogs.router, prefix="/blogs", tags=["Blog"])
router.include_router(users.router, prefix="/users", tags=["Users"])

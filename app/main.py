import time
from typing import List

from fastapi import Depends, FastAPI, HTTPException

from app.db import crud, config, models, schema
from app.db.config import db_state_default


config.db.connect()

config.db.create_tables([models.User, models.Blog])

config.db.close()


app = FastAPI()

sleep_time = 10


async def reset_db_state():
    config.db._state._state.set(db_state_default.copy())
    config.db._state.reset()


def get_db(db_state=Depends(reset_db_state)):
    try:
        config.db.connect()
        yield
    finally:
        if not config.db.is_closed():
            config.db.close()


@app.post("/users/", response_model=schema.User, dependencies=[Depends(get_db)])
def create_user(user: schema.UserCreate):
    db_user = crud.get_user_by_email(email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(user=user)


@app.get("/users/", response_model=List[schema.User], dependencies=[Depends(get_db)])
def read_users(skip: int = 0, limit: int = 100):
    users = crud.get_users(skip=skip, limit=limit)
    return users


@app.get(
    "/users/{user_id}", response_model=schema.User, dependencies=[Depends(get_db)]
)
def read_user(user_id: int):
    db_user = crud.get_user(user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post(
    "/users/{user_id}/blogs/",
    response_model=schema.Blog,
    dependencies=[Depends(get_db)],
)
def create_blog_for_user(user_id: int, blog: schema.BlogCreate):
    return crud.create_user_blog(blog=blog, user_id=user_id)


@app.get("/blogs/", response_model=List[schema.Blog], dependencies=[Depends(get_db)])
def read_blogs(skip: int = 0, limit: int = 100):
    blogs = crud.get_blogs(skip=skip, limit=limit)
    return blogs


@app.get(
    "/slowusers/", response_model=List[schema.User], dependencies=[Depends(get_db)]
)
def read_slow_users(skip: int = 0, limit: int = 100):
    global sleep_time
    sleep_time = max(0, sleep_time - 1)
    time.sleep(sleep_time)  # Fake long processing request
    users = crud.get_users(skip=skip, limit=limit)
    return users

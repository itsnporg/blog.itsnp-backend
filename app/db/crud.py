from app.db import models, schema


def get_user(user_id: int):
    return models.User.filter(models.User.id == user_id).first()


def get_user_by_email(email: str):
    return models.User.filter(models.User.email == email).first()


def get_users(skip: int = 0, limit: int = 100):
    return list(models.User.select().offset(skip).limit(limit))


def create_user(user: schema.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(
        email=user.email, hashed_password=fake_hashed_password)
    db_user.save()
    return db_user


def get_blogs(skip: int = 0, limit: int = 100):
    return list(models.Blog.select().offset(skip).limit(limit))


def create_user_blog(blog: schema.BlogCreate, user_id: int):
    db_item = models.Blog(**blog.dict(), user_id=user_id)
    db_item.save()
    return db_item

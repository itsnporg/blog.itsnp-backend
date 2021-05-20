from app.db.crud.base import CRUDBase
from app.db.models.blog import Blog
from app.schemas.blog import BlogCreate, BlogUpdate


class CRUDBlog(CRUDBase[Blog, BlogCreate, BlogUpdate]):
    pass


crud_blog = CRUDBlog(Blog)

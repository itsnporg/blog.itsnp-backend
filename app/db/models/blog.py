import sqlalchemy as sa
from app.db.session import Base


class Blog(Base):
    __tablename__ = "blogs"

    id = sa.Column(sa.Integer, primary_key=True, index=True)
    title = sa.Column(sa.String, index=True)
    body = sa.Column(sa.Text)

# blog.itsnp-backend

## Steps to run this project

``` 

Clone it: git clone https://github.com/itsnporg/blog.itsnp-backend.git 
Install dependencies: pip install -r requirements.txt 

Create .env in root and follow .env.template

Create a new database in postgres

Create tables using alembic:
alembic revision autogenerate -m "Initial Tables"
alembic upgrade head

Run App: uvicorn app.main:app --reload

```

### SQLAlchemy implementation with alembic(migration tool) and postgresql as database.

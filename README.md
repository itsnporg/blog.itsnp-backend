# blog.itsnp-backend

## Steps to run this project

``` 

Clone it: git clone https://github.com/itsnporg/blog.itsnp-backend.git 
Install dependencies: pip install -r requirements.txt 

Create .env in root and add follow .env.template

Create tables:
alembic revision autogenerate -m "Initial Tables"
alembic upgrade head

Run App: uvicorn app.main:app --reload

```

### Using peewee ORM right now. NOT SQLAlchemy. Not fixed tho.

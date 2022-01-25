from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


#from app.config import DATABASE_HOST, DATABASE_NAME, DATABASE_PASSWORD, DATABASE_USER

DATABASE_URL = "mysql+mysqldb://prod:prod@mysql/product"

db_engine = create_engine(DATABASE_URL)
Session = sessionmaker(autocommit=False, autoflush=False, bind=db_engine)

Base = declarative_base()



def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()
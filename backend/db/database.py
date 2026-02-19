from sqlalchemy import create_engine ## created engine to connect to the database (wrap the dfatabase we are connecting to)
from sqlalchemy.ext.declarative import declarative_base ##base class for our models to inherit (classes that represent tables in the database)
from sqlalchemy.orm import sessionmaker ## create a session to interact with the database
from core.config import settings

engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base() ##base class for our models to inherit (to give all the properties to work with the sql orm)

def get_db(): ## gice access to db session and ensure there are no multiple connections to the database at the same time (close the connection after use)
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_tables():##whene we first create the app we need to create tables in the database based on the models defined in the application (create tables if they do not exist)
    Base.metadata.create_all(bind=engine)
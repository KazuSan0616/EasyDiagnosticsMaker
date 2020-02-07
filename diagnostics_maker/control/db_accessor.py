from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound

engine = create_engine('sqlite://sample_db.sqlite3', echo=True)

Base = declarative_base()

class Diagnostic(Base):
    __tablename__ = 'diagnostics'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    text = Column(String)

Base.metadata.create_all(bind=engine)

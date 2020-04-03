from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound

Base = declarative_base()


class DbAccessor:
    def __init__(self):
        self.engine = create_engine("sqlite:///sample_db.sqlite3", echo=True)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
        Base.metadata.create_all(self.engine)

class Diagnostic(Base):
    __tablename__ = "diagnostics"

    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    baseText = Column(String(500))

class DiagnosticLists(Base):
    __tablename__ = "diagnosticslists"

    id = Column(Integer, primary_key=True)
    diagId = Column(Integer)
    listItem =Column(String(100))


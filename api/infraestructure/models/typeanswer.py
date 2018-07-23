import uuid
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relation, backref, sessionmaker, relationship
from api.infraestructure.connection.DAOConnection import Base



class Typeanswer(Base):

    __tablename__ = 'typeanswer'
    uuid = Column('uuid', String, primary_key=True)
    name = Column('name', String(25))

    type = relationship("Question", back_populates="answer")


    def __init__(self):
        self.uuid = uuid.uuid4()

import uuid
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relation, backref, sessionmaker, relationship
from api.infraestructure.connection.DAOConnection import Base


class Course(Base):

    __tablename__ = 'courses'

    uuid = Column('uuid', String, primary_key=True)
    name = Column('name', String(25))
    depend = Column('depend', Integer)
    uuidCourse = Column('uuidCourse', String, default="")

    def __init__(self):
        self.uuid = uuid.uuid4()

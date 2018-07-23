import uuid
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relation, backref, sessionmaker, relationship
from api.infraestructure.connection.DAOConnection import Base



class Rol(Base):

    __tablename__ = 'roles'
    uuidRol = Column('uuid', String, primary_key=True)
    description = Column('description', String(25))

    user = relationship("User", uselist=False, back_populates="rol")


    def __init__(self):
        self.uuidRol = uuid.uuid4()

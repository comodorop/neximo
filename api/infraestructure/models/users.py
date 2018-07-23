import uuid
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relation, backref, sessionmaker, relationship
from api.infraestructure.connection.DAOConnection import Base

from api.infraestructure.models.rol import Rol



class User(Base):

    __tablename__ = 'users'

    uuid = Column('uuid', String, primary_key=True)
    user = Column('user', String(25))
    password = Column('password', String(80))

    uuidRol = Column('uuidRol', String, ForeignKey('roles.uuid'))
    rol = relationship("Rol", back_populates="user")

    def __init__(self):
        self.uuidUser = uuid.uuid4()

import uuid
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relation, backref, sessionmaker, relationship
from api.infraestructure.connection.DAOConnection import Base


class Lesson(Base):

    __tablename__ = 'lessons'
    uuid = Column('uuid', String, primary_key=True)




    uuidCourse = Column('uuidCourse', String(25), ForeignKey('courses.uuid'))
    courses = relationship(
        "Course", backref=backref('courses', uselist=True))


    name = Column('name', String(25))
    depend = Column('depend', Integer,  default=False)
    uuidLesson = Column('uuidLesson', String, default= "")

    def __init__(self):
        self.uuid = uuid.uuid4()

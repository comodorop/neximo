import uuid
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relation, backref, sessionmaker, relationship
from api.infraestructure.connection.DAOConnection import Base
from api.infraestructure.models.typeanswer import Typeanswer



class Question(Base):

    __tablename__ = 'questions'
    uuid = Column('uuid', String, primary_key=True)
    question = Column('question', String(25))
    score = Column('score', Integer)

    uuidType = Column('uuidType', String, ForeignKey(Typeanswer.uuid))
    answer = relationship("Typeanswer", uselist=False, back_populates="type")


    uuidLesson = Column('uuidLesson', String(25), ForeignKey('lessons.uuid'))
    lesson = relationship(
        "Lesson", backref=backref('lessons', uselist=True))

    def __init__(self):
        self.uuid = uuid.uuid4()

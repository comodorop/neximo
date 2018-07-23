import uuid
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relation, backref, sessionmaker, relationship
from api.infraestructure.connection.DAOConnection import Base
from api.infraestructure.models.questions import Question


class Answer(Base):
    __tablename__ = 'answers'

    uuid = Column('uuid', String, primary_key=True)
    answer = Column('answer', String(25))
    isCorrect = Column('isCorrect', Integer)

    uuidQuestion = Column('uuidQuestion', String(25), ForeignKey(Question.uuid))
    question = relationship(
        "Question", backref=backref('questions', uselist=True))




    def __init__(self):
        self.uuid = uuid.uuid4()

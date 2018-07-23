from api.infraestructure.models.rol import Rol
from api.infraestructure.models.users import User
from api.infraestructure.models.course import Course
from api.infraestructure.models.lesson import Lesson
from api.infraestructure.models.questions import Question
from api.infraestructure.models.typeanswer import Typeanswer
from api.infraestructure.models.answer import Answer
import uuid


class Converter(object):

    def converterUsers(self, jsonData):
        user = User()
        if 'uuid' in jsonData:
            user.uuid = jsonData["uuid"]
        else:
            user.uuid = uuid.uuid4()
        user.password = jsonData["password"]
        user.uuidRol = jsonData["uuidRol"]
        user.user = jsonData["user"]
        return user

    def converterCourse(self, jsonData):
        course = Course()
        if 'uuid' in jsonData:
            course.uuid = jsonData["uuid"]
        else:
            course.uuid = uuid.uuid4()
        course.name = jsonData["name"]
        course.depend = str(jsonData["depend"])
        course.uuidCourse = jsonData["uuidCourse"]
        return course

    def converterLesson(self, jsonData):
        lesson = Lesson()
        if 'uuid' in jsonData:
            lesson.uuid = jsonData["uuid"]
        else:
            lesson.uuid = uuid.uuid4()
        lesson.uuidCourse = jsonData["uuidCourse"]
        lesson.name = jsonData["name"]
        lesson.depend = jsonData["depend"]
        lesson.uuidLesson = jsonData["uuidLesson"]
        return lesson

    def converterQuestions(self, jsonData):
        question = Question()
        if 'uuid' in jsonData:
            question.uuid = jsonData["uuid"]
        else:
            question.uuid = uuid.uuid4()
        question.question = jsonData["question"]
        question.score = jsonData["score"]
        question.uuidLesson = jsonData["uuidLesson"]
        return question

    def converterTypeAnswer(self, jsonData):
        type = Typeanswer()
        if 'uuid' in jsonData:
            type.uuid = jsonData["uuid"]
        else:
            type.uuid = uuid.uuid4()
        type.name = jsonData["name"]
        return type

    def converterAnswer(self, jsonData):
        answer = Answer()
        if 'uuid' in jsonData:
            answer.uuid = jsonData["uuid"]
        else:
            answer.uuid = uuid.uuid4()
        answer.answer = jsonData["answer"]
        answer.isCorrect = jsonData["isCorrect"]
        answer.uuidQuestion = jsonData["uuidQuestion"]
        return answer






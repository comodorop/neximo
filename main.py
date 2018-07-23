import falcon
from falcon_cors import CORS
from api.infraestructure.connection.DAOConnection import Base,Session,engine
from api.use_case.use_case_users import User
from api.use_case.use_case_course import Course
from api.use_case.use_case_lesson import Lesson
from api.use_case.use_case_questions import Questions
from api.use_case.use_case_typeAnswerd import TypeAnswer
from api.use_case.use_case_answer import Answer



public_cors = CORS(allow_all_origins=True,  allow_all_headers=True,allow_all_methods=True)
middleware = [
        public_cors.middleware
]

app = falcon.API(middleware=middleware)
Base.metadata.create_all(engine)
obj_login = User()
obj_course = Course()
obj_lesson = Lesson()
obj_questions = Questions()
obj_type_answer = TypeAnswer()
obj_answer = Answer()

app.add_route("/login", obj_login)
app.add_route("/course", obj_course)
app.add_route("/lesson", obj_lesson)
app.add_route("/questions", obj_questions)
app.add_route("/type", obj_type_answer)
app.add_route("/answer", obj_answer)



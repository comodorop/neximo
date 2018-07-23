
from api.applications.interface.actions_data_base import ActionsDataBase
from api.infraestructure.models.course import Course
from api.infraestructure.connection.DAOConnection import Base,  Session, engine
from api.infraestructure.utis.Message import Message
from sqlalchemy import exc

Base.metadata.create_all(engine)



class DAOCourse(ActionsDataBase):
    obj_sesion = ""
    objCourse = Course()
    msg = Message()

    def __init__(self):
        self.obj_sesion = Session()

    def save(self, obj_course):
        print("ESTE ES EL OBJETO")
        print(obj_course.depend)
        try:
            self.obj_sesion.add(obj_course)
            self.obj_sesion.commit()
            return self.msg.message('200', "New register")
        except exc.SQLAlchemyError as e :
            self.obj_sesion.rollback()
            return self.msg.message('400', "Este registro ya esta disponible")




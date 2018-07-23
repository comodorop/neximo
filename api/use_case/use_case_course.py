from api.interface_adapter.converterData import Converter
from api.infraestructure.persistent.DAOCourse import DAOCourse
import json
import falcon


class Course(object):



    def on_post(self, req, resp):
        daoCourse = DAOCourse()
        converter = Converter()
        obj_course = converter.converterCourse(json.load(req.stream))
        print("************ESTOS  SON LOS VALORES DEL CONVERTER*************")
        print(obj_course.depend)
        data = daoCourse.save(obj_course)
        resp.body = json.dumps(data)




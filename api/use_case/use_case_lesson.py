from api.interface_adapter.converterData import Converter
from api.infraestructure.persistent.DAOLesson import DAOLesson
import json
import falcon


class Lesson(object):



    def on_post(self, req, resp):
        daoLeson = DAOLesson()
        converter = Converter()
        obj_course = converter.converterLesson(json.load(req.stream))
        data = daoLeson.save(obj_course)
        resp.body = json.dumps(data)




from api.interface_adapter.converterData import Converter
from api.infraestructure.persistent.DAOQuestions import DAOQuestions
import json
import falcon


class Questions(object):



    def on_post(self, req, resp):
        daoQuestion = DAOQuestions()
        converter = Converter()
        obj_questions = converter.converterQuestions(json.load(req.stream))
        data = daoQuestion.save(obj_questions)
        resp.body = json.dumps(data)




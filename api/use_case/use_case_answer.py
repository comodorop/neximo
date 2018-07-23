from api.interface_adapter.converterData import Converter
from api.infraestructure.persistent.DAOAnswer import DAOAnswer
import json
import falcon


class Answer(object):



    def on_post(self, req, resp):
        daoAnswer = DAOAnswer()
        converter = Converter()
        obj_answer = converter.converterAnswer(json.load(req.stream))
        data = daoAnswer.save(obj_answer)
        resp.body = json.dumps(data)




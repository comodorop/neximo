from api.interface_adapter.converterData import Converter
from api.infraestructure.persistent.DAOTypeAnswer import DAOType
import json
import falcon


class TypeAnswer(object):



    def on_post(self, req, resp):

        dao_type = DAOType()
        converter = Converter()
        obj_type = converter.converterTypeAnswer(json.load(req.stream))
        data = dao_type.save(obj_type)
        resp.body = json.dumps(data)




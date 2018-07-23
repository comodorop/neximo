from api.interface_adapter.converterData import Converter
from api.infraestructure.persistent.DAOUser import DAOUser
import json
import falcon


class User(object):



    def on_post(self, req, resp):

        daoUser = DAOUser()
        converter = Converter()
        obj_user = converter.converterUsers(json.load(req.stream))
        print("***************ENTRO AL POST*****************")
        data = daoUser.select(obj_user)
        print("ESTA ES LA INFORMACION DEL DATA**********************")
        print(data)
        print(type(data))
        resp.body = json.dumps(data)




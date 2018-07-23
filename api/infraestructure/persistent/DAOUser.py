
from api.applications.interface.actions_data_base import ActionsDataBase
from api.infraestructure.models.users import User
from api.infraestructure.models.rol import Rol
from api.infraestructure.connection.DAOConnection import Base,  Session, engine
from api.infraestructure.utis.Message import Message
from api.infraestructure.utis.token import Token
import json

Base.metadata.create_all(engine)


class DAOUser(ActionsDataBase):

    obj_sesion = ""
    objUser = User()
    msg = Message()

    def __init__(self):
        self.obj_sesion = Session()

    def select(self, obj):
        lstInfo = []
        data = self.obj_sesion.query(User).filter(User.user == obj.user).first()
        if data is not None:
            token = Token()
            value_token = token.generate_token(data.user, data.password)
            obj_info = {
                'token': value_token,
                'status': 201
            }
            lstInfo.append(obj_info)
            return self.msg.message("200", "Acceso correcto", lstInfo)
        else:
            return self.msg.message("200", "Credenciales Invalidas", [])

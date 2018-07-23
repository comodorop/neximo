import json

class Message:

    def message(self,status,msg, data=[]):
        msg = {
            "status": status,
            "msg": msg,
            "data": data
        }
        return msg


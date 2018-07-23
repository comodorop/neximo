import jwt
import ujson


class Token:

    def generate_token(self, user, password):
        encode = jwt.encode({"user":user, "password": password}, 'secret', algorithm='HS256')
        return ujson.dumps(encode)

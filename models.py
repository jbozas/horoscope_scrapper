from receivers import Receivers, Signs


class User(object):
    name: str
    number: int
    sign: str

    def __init__(self, name, number, sign):
        self.name = name
        self.number = number
        self.sign = sign


class Sign(object):
    name: str
    url: str
    message: str

    def __init__(self, name, url, message):
        self.name = name
        self.url = url
        self.message = message


class DataManager(object):

    def _init_users(self):
        for receiver in Receivers:
            self.users.append(
                User(receiver.get('name'), receiver.get(
                    'number'), receiver.get('sign'))
            )

    def _init_signs(self):
        for sign in Signs:
            self.signs.append(
                Sign(name=sign, url='', message='')
            )

    def __init__(self):
        self.signs = []
        self.users = []
        self._init_signs()
        self._init_users()

    def get_sign(self, sign: str) -> Sign:
        for s in self.signs:
            if s.name == sign:
                return s

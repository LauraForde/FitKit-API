import requests
login = {
    "_id":"1234",
    "name":"Laura",
    "password":"1234"
}

class CouchProvider(object):
    def read_login(self) -> str:
        return login,1

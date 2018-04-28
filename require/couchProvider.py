import requests
import couchdb
ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = 'pass'
COUCHDB_URL = 'http://54.68.14.217:5000/'
#COUCHDB_URL = 'http://54.68.14.217:5984/'
couch = couchdb.Server(os.environ['SERVER_URL'])


class CouchProvider(object):
    def create_user(self,payload):
        db = couch['login']
        if payload['_id'] in db:
            return {"error":"This username is taken!"},409
        else:
            db.save(payload)
            return payload,201
    
    def read_user(self):
        db = couch['login']
        if(user_id in db):
            user = db[user_id]
            return user, 200
        else:
            return {"error": "User not found."}, 400
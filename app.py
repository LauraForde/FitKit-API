import os
import connexion
#from flask_injector import FlaskInjector
from connexion.resolver import RestyResolver
#from providers.CouchProvider import CouchProvider
#from injector import Binder

import requests
import couchdb
ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = 'pass'
COUCHDB_URL = 'http://'+ADMIN_USERNAME+':'+ADMIN_PASSWORD+'@localhost:5984/'
couch = couchdb.Server(COUCHDB_URL)

def configure(Binder):
    binder.bind(
        CouchProvider
    )

class CouchProvider(object):
    def create_user(self,payload):
        db = couch['login']
        if payload['_id'] in db:
            return {"error":"This username is taken!"},409
        else:
            db.save(payload)
            return payload,201
    
    def read_user(self, user_id):
        db = couch['login']
        if(user_id in db):
            user = db[user_id]
            return user, 200
        else:
            return {"error": "User not found."}, 400


if __name__ == '__main__':
    app = connexion.App(__name__, arguments={'global':'global_value'})  # Provide the app and the directory of the docs specification_dir='swagger/'
    app.add_api('swagger.yaml', arguments={'api_local': 'local_value'})
    #FlaskInjector(app=app.app, modules=[configure])
    app.run(port = 2020) 
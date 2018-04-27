import os
import connexion
import logging
#from flask_injector import FlaskInjector
from connexion.resolver import RestyResolver
from providers.CouchProvider import CouchProvider
#from injector import Binder
from connexion.apis import flask_utils
from connexion.apis.abstract import AbstractAPI
from connexion.decorators.produces import NoContent
from connexion.handlers import AuthErrorHandler
from connexion.lifecycle import ConnexionRequest, ConnexionResponse
from connexion.utils import Jsonifier, is_json_mimetype

logger = logging.getLogger('connexion.apis.app')

app = connexion.App(__name__, specification_dir='swagger/')
app.add_api('swagger.yaml', resolver=RestyResolver('providers'))

if __name__ == '__main__':
    app = connexion.App(__name__, specification_dir='swagger/')  # Provide the app and the directory of the docs specification_dir='swagger/'
    app.add_api('swagger.yaml', arguments={'title': 'RestyResolver Example'}, resolver = RestyResolver('providers'))
    #FlaskInjector(app=app.app, modules=[configure])
    app.run(port = int(os.environ.get('POST', 2020))) 

#specification_dir='swagger/'
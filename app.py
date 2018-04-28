import os
import connexion
#from flask_injector import FlaskInjector
from connexion.resolver import RestyResolver
from providers.couchProvider import CouchProvider
#from injector import Binder
#app = connexion.App(__name__, specification_dir='swagger/')
#app.add_api('swagger.yaml', resolver=RestyResolver('providers'))
import logging

logger = logging.getLogger('connexion.apis.app')


if __name__ == '__main__':
    
    logger.debug('what')
    app = connexion.App(__name__, specification_dir='swagger/')  # Provide the app and the directory of the docs specification_dir='swagger/'
    app.add_api('swagger.yaml', arguments={'title': 'RestyResolver Example'}, resolver = RestyResolver('providers'))
    #FlaskInjector(app=app.app, modules=[configure])
    app.run(port = int(os.environ.get('POST', 5000))) 

#specification_dir='swagger/'
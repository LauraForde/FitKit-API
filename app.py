import os
import connexion
from flask_cors import CORS
from connexion.resolver import RestyResolver
from providers.couchProvider import CouchProvider
#from injector import Binder
#app = connexion.App(__name__, specification_dir='swagger/')
#app.add_api('swagger.yaml', resolver=RestyResolver('providers'))
import logging

app = Flask(__name__)
CORS(app)

logger = logging.getLogger('connexion.apis.app')
app.add_api('swagger.yaml', arguments={'title': 'RestyResolver Example'}, resolver = RestyResolver('providers'))

if __name__ == '__main__':
    
    logging.getLogger('flask_cors').level = logging.DEBUG
    app = connexion.App(__name__, specification_dir='swagger/')  # Provide the app and the directory of the docs specification_dir='swagger/'
    #FlaskInjector(app=app.app, modules=[configure])
    app.run(debug = True, port = int(os.environ.get('POST', 5000))) 

#specification_dir='swagger/'
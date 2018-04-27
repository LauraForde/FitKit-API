import os
import connexion
#from flask_injector import FlaskInjector
from connexion.resolver import RestyResolver
from providers.CouchProvider import CouchProvider
#from injector import Binder
app = connexion.App(__name__, specification_dir='swagger/')
app.add_api('swagger.yaml', resolver=RestyResolver('providers'))

if __name__ == '__main__':
    app = connexion.App(__name__, specification_dir='swagger/')  # Provide the app and the directory of the docs specification_dir='swagger/'
    app.add_api('swagger.yaml', arguments={'title': 'RestyResolver Example'}, resolver = RestyResolver('providers'))
    #FlaskInjector(app=app.app, modules=[configure])
    app.run(port = int(os.environ.get('POST', 2020))) 

#specification_dir='swagger/'
import os
import connexion
#from flask_injector import FlaskInjector
from connexion.resolver import RestyResolver
from providers.CouchProvider import CouchProvider

from injector import Binder

def configure(Binder):
    binder.bind(
        CouchProvider
    )


if __name__ == '__main__':
    app = connexion.App(__name__)  # Provide the app and the directory of the docs specification_dir='swagger/'
    app.add_api('swagger.yaml', resolver=RestyResolver('api'))
    #FlaskInjector(app=app.app, modules=[configure])
    app.run(port=int(os.environ.get('PORT', 2020))) 
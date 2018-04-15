from flask_injector import flask_injector
from providers.CouchProvider import CouchProvider

@inject(data_provider=CouchProvider)
def read_users(data_provider) -> str:
    return data_provider.read_login()
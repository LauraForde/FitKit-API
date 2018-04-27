from flask_injector import inject
from providers.couchProvider import CouchProvider
import flask

from flask import request, Response

@inject(data_provider=CouchProvider)
def read_user(data_provider):
    return data_provider.read_user()
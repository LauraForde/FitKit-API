from providers.couchProvider import CouchProvider
import flask

from flask import request, Response

data_provider=CouchProvider
def read_user(data_provider):
    return data_provider.read_user()
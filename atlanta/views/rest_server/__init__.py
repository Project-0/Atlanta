#!/usr/bin/env python

""" Defines Atlanta's built-in REST interface """

from flask import Flask
from flask_restful import Api, Resource


class PingTest(Resource):
    """ Provides a minimal (almost nihilistic) REST endpoint """

    def get(self, say='test'):
        """ Returns a JSON oject and HTTP_200 """
        return {'ping': say}

    def post(self):
        """ Still needs to be implemented """
        pass


class AtlantaREST(object):
    """ Provides an instance of a RESTful interface

    TODO: This clas should end up being a wrapper around a Flask app, I expect.
    We will need to define the endpoints and things in an
    """

    app = None
    api = None

    def __init__(self, name="atlanta"):
        self.app = Flask(name)
        self.api = Api(self.app)
        self.api.add_resource(PingTest, '/ping', '/ping/<string:say>',
                              endpoint='ping')

    @classmethod
    def run(cls):
        atlanta = cls()
        atlanta.app.run()

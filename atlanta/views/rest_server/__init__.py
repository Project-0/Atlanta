#!/usr/bin/env python

""" Defines Atlanta's built-in REST interface """

from eve import Eve


class AtlantaREST(object):
    """ Provides an instance of a RESTful interface

    TODO: This class should end up being a wrapper around a Flask app, I expect.
    We will need to define the endpoints and things in an
    """

    rest_api = None

    def __init__(self, name="atlanta"):
        self.rest_api = Eve()

    @classmethod
    def run(cls):
        atlanta = cls()
        atlanta.rest_api.run(host="192.168.1.137", port=5050)

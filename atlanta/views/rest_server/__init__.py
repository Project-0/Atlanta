#!/usr/bin/env python

""" Defines Atlanta's built-in REST interface """

from eve import Eve


class AtlantaREST(object):
    """ Provides an instance of a RESTful interface

    TODO: This clas should end up being a wrapper around a Flask app, I expect.
    We will need to define the endpoints and things in an
    """

    app = None

    def __init__(self, name="atlanta"):
        self.app = Eve()

    @classmethod
    def run(cls):
        atlanta = cls()
        atlanta.app.run(host="192.168.1.137", port=5050)

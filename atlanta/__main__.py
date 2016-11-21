#!/usr/bin/env python

""" Initializes the CLI interface for Atlanta """

import argparse

from atlanta.views.rest_server import AtlantaREST
from atlanta.views.flask_server import FlaskServer


class Application(argparse.ArgumentParser):

    def __init__(self, **kwargs):
        super(Application, self).__init__(**kwargs)

        self.rest_parser = self.add_subparsers('rest', help='manages the local REST (api) service')
        self.rest_parser.set_defaults(func=FlaskServer.run)

        self.http_parser = self.add_subparsers('http', help='manages the local HTTP (static web) service')


def main():
    server = AtlantaREST()
    server.app.run(host='0.0.0.0')

if __name__ == "__main__":
    main()

#!/usr/bin/env python

""" Initializes the CLI interface for Atlanta """

from atlanta.views.rest_server import AtlantaREST


def main():
    server = AtlantaREST()
    server.app.run()

if __name__ == "__main__":
    main()

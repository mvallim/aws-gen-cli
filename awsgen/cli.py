import sys

from app import App

class CLI(object):

    def run(self, argv=None):
        App().run(argv)
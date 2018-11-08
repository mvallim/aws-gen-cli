import logging

from awsgen.applications.profile import ProfileApp

class ListProfiles(object):

    log = logging.getLogger(__name__)

    def __init__(self, parser=None):
        pass
        
    def action(self, args):
        ProfileApp().list()

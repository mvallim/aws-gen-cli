import logging

from awsgen.applications.profile import ProfileApp

class SetActiveProfile(object):

    log = logging.getLogger(__name__)

    def __init__(self, parser=None):
        parser.add_argument('--profile', metavar='profile', required=True, dest='profile')

        
    def action(self, args):
        ProfileApp().setActive(args.profile)

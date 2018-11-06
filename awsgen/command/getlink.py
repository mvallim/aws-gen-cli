import logging

from awsgen.models.request import Request

from awsgen.applications.temporary import TemporaryApp

class GetLink(object):

    log = logging.getLogger(__name__)

    def __init__(self, parser):
        parser.add_argument('--account', metavar='account', required=True, dest='account')
        parser.add_argument('--profile', metavar='profile', required=True, dest='profile')


    def action(self, args):
        request = Request(
            profile = args.profile, 
            sourceProfile = args.account
        )

        print('')
        print('Magic Link: ' + TemporaryApp().link(request))
        print('')

import logging

from awsgen.models.request import Request

from awsgen.applications.temporary import TemporaryApp

class GetKey(object):

    log = logging.getLogger(__name__)

    def __init__(self, parser):
        parser.add_argument('--account', metavar='account', required=True, dest='account')
        parser.add_argument('--profile', metavar='profile', required=True, dest='profile')


    def action(self, args):
        request = Request(
            profile = args.profile, 
            sourceProfile = args.account
        )

        credentials = TemporaryApp().key(request)

        print('')
        print('')
        print('Linux, macOS, or Unix')
        print('')
        print('export AWS_ACCESS_KEY_ID=' + credentials.accessKeyId)
        print('export AWS_SECRET_ACCESS_KEY=' + credentials.secretAccessKey)
        print('export AWS_SESSION_TOKEN=' + credentials.sessionToken)
        print('')
        print('')
        print('Windows')
        print('')
        print('set AWS_ACCESS_KEY_ID=' + credentials.accessKeyId)
        print('set AWS_SECRET_ACCESS_KEY=' + credentials.secretAccessKey)
        print('set AWS_SESSION_TOKEN=' + credentials.sessionToken)
        print('')

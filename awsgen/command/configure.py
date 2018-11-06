import logging

from awsgen.models.account import Account
from awsgen.models.profile import Profile
from awsgen.models.credentials import Credentials

from awsgen.applications.profile import ProfileApp
from awsgen.applications.account import AccountApp

class Configure(object):

    log = logging.getLogger(__name__)

    def __init__(self, parser):
        parser.add_argument('--account', required=True, dest='account')
        parser.add_argument('--trust-role-arn', required=True, dest='trustRoleArn')
        parser.add_argument('--access-key-id', required=True, dest='accessKeyId')
        parser.add_argument('--secret-access-key', required=True, dest='secretAccessKey')


    def action(self, args):
        credentials = Credentials(
            accessKeyId = args.accessKeyId, 
            secretAccessKey = args.secretAccessKey
        )

        profile = Profile(
            name = args.account,
            credentials = credentials
        )

        account = Account(
            name = args.account, 
            trustRoleArn = args.trustRoleArn
        )

        ProfileApp().save(profile)
        AccountApp().save(account)

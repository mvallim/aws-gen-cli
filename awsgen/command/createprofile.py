import logging

from awsgen.models.request import Request
from awsgen.models.profile import Profile
from awsgen.models.configuration import Configuration

from awsgen.applications.profile import ProfileApp
from awsgen.applications.account import AccountApp
from awsgen.applications.configuration import ConfigurationApp

class CreateProfile(object):

    log = logging.getLogger(__name__)

    def __init__(self, parser):
        parser.add_argument('--account', required=True, dest='account')
        parser.add_argument('--profile', required=True, dest='profile')
        parser.add_argument('--region-name', required=True, dest='region')
        parser.add_argument('--output', required=True, dest='output')


    def action(self, args):
        account = AccountApp().get(args.account)

        profile = Profile(
            name = args.profile, 
            trustRoleArn = account.trustRoleArn, 
            sourceProfile = args.account
        )

        configuration = Configuration(
            profile = args.profile, 
            region = args.region, 
            output = args.output
        )

        ProfileApp().save(profile)
        ConfigurationApp().save(configuration)

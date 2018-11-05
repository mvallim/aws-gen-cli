import os
import sys
import logging

from awsgen.models.configuration import Configuration
from awsgen.models.credentials import Credentials
from awsgen.models.request import Request

from awsgen.applications.configuration import ConfigurationApplication
from awsgen.applications.credentials import CredentialsApplication

class Configure(object):

    log = logging.getLogger(__name__)

    def __init__(self, parser):
        parser.add_argument('--role-arn', metavar='arn:aws:iam::xxxxxxxxxxxx:role/AWSTrustUserRole', required=True, dest='roleArn')
        parser.add_argument('--cloudformation-role-arn', metavar='arn:aws:iam::xxxxxxxxxxxx:role/AWSCloudFormationPassRole', required=True, dest='cloudformationRoleArn')
        parser.add_argument('--session-name', metavar='foo@account', required=True, dest='sessionName')
        parser.add_argument('--profile', metavar='account', required=True, dest='profileName')
        parser.add_argument('--region-name', metavar='us-east-1', default='us-east-1', required=True, dest='regionName', 
            choices=[
                'ap-northeast-1', 'ap-northeast-2', 'ap-northeast-3',
                'ap-south-1', 'ap-southeast-1', 'ap-southeast-2',
                'ca-central-1', 'cn-north-1', 'cn-northwest-1',
                'eu-central-1', 'eu-west-1', 'eu-west-2',
                'eu-west-3', 'sa-east-1', 'us-east-1',
                'us-east-2', 'us-west-1', 'us-west-2'])

    def action(self, args):
        credentialsApplication = CredentialsApplication()
        configurationApplication = ConfigurationApplication()
        request = Request(args.roleArn, args.sessionName, args.profileName)
        credentials = credentialsApplication.getCredentials(request=request)
        configuration = Configuration(args.sessionName, args.cloudformationRoleArn, args.regionName, credentials)
        configurationApplication.save(configuration=configuration)
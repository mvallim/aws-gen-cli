import os
import sys
import logging

from awsgen.models.credentials import Credentials
from awsgen.models.request import Request

from awsgen.applications.credentials import CredentialsApplication

class Link(object):

    log = logging.getLogger(__name__)

    def __init__(self, parser):
        parser.add_argument('--role-arn', metavar='arn:aws:iam::xxxxxxxxxxxx:role/AWSTrustUserRole', required=True, dest='roleArn')
        parser.add_argument('--session-name', metavar='foo@account', required=True, dest='sessionName')
        parser.add_argument('--profile', metavar='account', required=True, dest='profileName')

    def action(self, args):
        credentialsApplication = CredentialsApplication()
        request = Request(args.roleArn, args.sessionName, args.profileName)
        credentials = credentialsApplication.getCredentials(request=request)
        print('')
        print('\tMagic Link: ' + credentialsApplication.getConsoleLink(credentials=credentials))
        print('')

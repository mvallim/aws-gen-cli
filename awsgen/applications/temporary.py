import os
import sys
import boto3
import json
import requests

from configparser import ConfigParser

from botocore.exceptions import ClientError

from awsgen.models.credentials import Credentials

from awsgen.applications.account import AccountApp

class TemporaryApp(object):

    def key(self, request):
        account = AccountApp().get(request.sourceProfile)
        boto3.setup_default_session(profile_name=request.sourceProfile)
        sts = boto3.client('sts')
        try:
            response = sts.assume_role(RoleArn=account.trustRoleArn, RoleSessionName=request.profile)
            credentials = Credentials(
                secretAccessKey=response['Credentials']['SecretAccessKey'],
                sessionToken=response['Credentials']['SessionToken'],
                accessKeyId=response['Credentials']['AccessKeyId']
            )
            return credentials
        except ClientError:
            print('')
            print('\tThe request signature we calculated does not match the signature you provided.')
            print('\tCheck your AWS Secret Access Key and signing method on profile [' + request.profile + ']')
            print('\tCheck your Arn role [' + account.trustRoleArn + ']')
            print('')
            sys.exit(1)


    def link(self, request):
        credentials = self.key(request)

        session = json.dumps({
            'sessionId': credentials.accessKeyId,
            'sessionKey': credentials.secretAccessKey,
            'sessionToken': credentials.sessionToken
        })

        request = requests.get("https://signin.aws.amazon.com/federation",
            params={
                'Action': 'getSigninToken',
                'SessionDuration': 43200,
                'Session': session
            }
        )

        signinToken = request.json()

        console = requests.Request('GET','https://signin.aws.amazon.com/federation',
            params={
                'Action': 'login',
                'Issuer': 'trustuser',
                'Destination': 'https://console.aws.amazon.com/',
                'SigninToken': signinToken['SigninToken']
            }
        )

        preparedLink = console.prepare()

        return preparedLink.url

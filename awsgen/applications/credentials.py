import sys
import boto3
import json
import requests

from botocore.exceptions import ClientError

from awsgen.models.credentials import Credentials

class CredentialsApplication(object):

    def getCredentials(self, request):
        boto3.setup_default_session(profile_name=request.profileName)
        sts = boto3.client('sts')
        try:
            response = sts.assume_role(RoleArn=request.roleArn, RoleSessionName=request.sessionName)
            credentials = Credentials(
                secretAccessKey=response['Credentials']['SecretAccessKey'],
                sessionToken=response['Credentials']['SessionToken'],
                accessKeyId=response['Credentials']['AccessKeyId']
            )
            return credentials
        except ClientError:
            print('')
            print('\tThe request signature we calculated does not match the signature you provided.')
            print('\tCheck your AWS Secret Access Key and signing method on profile [' + request.profileName + ']')
            print('\tCheck your Arn role [' + request.roleArn + ']')
            print('')
            sys.exit(1)


    def getConsoleLink(self, credentials):
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
import boto3
import json
import requests
from botocore.exceptions import ClientError

from colors import Colors
from ..models.credentials import Credentials

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
        except ClientError as e:
            print Colors.WARNING
            print '\t' + 'The request signature we calculated does not match the signature you provided.'
            print '\t' + 'Check your AWS Secret Access Key and signing method on profile [' + Colors.FAIL + Colors.BOLD + request.profileName + Colors.WARNING + ']'
            print '\t' + 'Check your Arn role [' + Colors.FAIL + Colors.BOLD + request.roleArn + Colors.WARNING + ']'
            print Colors.ENDC
            exit(0)


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
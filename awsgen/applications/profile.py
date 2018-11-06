import os

from configparser import ConfigParser

from awsgen.models.profile import Profile

class ProfileApp(object):

    def save(self, profile):
        self.__writeProfile(profile)


    def __writeProfile(self, profile):
        filename = os.path.expanduser('~/.aws/credentials')
        dirname = os.path.dirname(filename)

        if not os.path.exists(dirname):
            os.makedirs(dirname)

        config = ConfigParser()
        config.read(filename)

        if not config.has_section(profile.name):
            config.add_section(profile.name)

        if profile.trustRoleArn:
            config.set(profile.name, 'role_arn', profile.trustRoleArn)

        if profile.sourceProfile:
            config.set(profile.name, 'source_profile', profile.sourceProfile)

        if profile.credentials:
            if profile.credentials.accessKeyId:
                config.set(profile.name, 'aws_access_key_id', profile.credentials.accessKeyId)

            if profile.credentials.secretAccessKey:
                config.set(profile.name, 'aws_secret_access_key', profile.credentials.secretAccessKey)

            if profile.credentials.sessionToken:
                config.set(profile.name, 'aws_session_token', profile.credentials.sessionToken)

        with open(filename, 'w') as fp:
            config.write(fp)

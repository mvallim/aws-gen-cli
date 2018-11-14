import os

from configparser import ConfigParser

class ProfileApp(object):

    def save(self, profile):
        self.__writeProfile(profile)


    def setActive(self, profile):
        self.__writeActiveProfile(profile)


    def getActive(self):
        filename = os.path.expanduser('~/.aws/credentials')
        dirname = os.path.dirname(filename)

        if not os.path.exists(dirname):
            print('File: [' + filename + '] not found')
            return

        config = ConfigParser()
        config.read(filename)

        if not config.has_section('default'):
            print('Profile: [default] not found')
            return

        return config.get('default', 'active')

    def list(self):
        filename = os.path.expanduser('~/.aws/credentials')
        dirname = os.path.dirname(filename)

        if not os.path.exists(dirname):
            print('File: [' + filename + '] not found')
            return

        config = ConfigParser()
        config.read(filename)

        sections = sorted(config.sections())

        for section in sections:
            print('[' + section + ']')
            print('')


    def __writeActiveProfile(self, profile):
        filename = os.path.expanduser('~/.aws/credentials')
        dirname = os.path.dirname(filename)

        if not os.path.exists(dirname):
            print('File: [' + filename + '] not found')
            return

        config = ConfigParser()
        config.read(filename)

        if not config.has_section(profile):
            print('Profile: [' + profile + '] not found')
            return

        config.remove_section('default')
        config.add_section('default')

        for value in config.items(profile):
            config.set('default', value[0], value[1])

        config.set('default', 'active', profile)

        with open(filename, 'w') as fp:
            config.write(fp)


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

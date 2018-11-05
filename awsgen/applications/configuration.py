import os
import configparser

class ConfigurationApplication(object):

    def save(self, configuration):
        if not configuration.profile:
            raise AttributeError('property [profile] can not empty')

        if not configuration.region:
            raise AttributeError('property [region] can not empty')

        if not configuration.credentials:
            raise AttributeError('property [credentials] can not empty')

        if not configuration.credentials.accessKeyId:
            raise AttributeError('property [credentials.accessKeyId] can not empty')

        if not configuration.credentials.secretAccessKey:
            raise AttributeError('property [credentials.secretAccessKey] can not empty')

        if not configuration.credentials.sessionToken:
            raise AttributeError('property [credentials.sessionToken] can not empty')

        self.__writeCredentials(configuration)
        self.__writeRegion(configuration)

        pass

    def __writeCredentials(self, configuration):
        filename = os.path.expanduser('~/.aws/credentials')
        dirname = os.path.dirname(filename)

        if not os.path.exists(dirname):
            os.makedirs(dirname)

        config = configparser.ConfigParser()
        config.read(filename)

        if not config.has_section(configuration.profile):
            config.add_section(configuration.profile)

        config.set(configuration.profile, 'aws_access_key_id', configuration.credentials.accessKeyId)
        config.set(configuration.profile, 'aws_secret_access_key', configuration.credentials.secretAccessKey)
        config.set(configuration.profile, 'aws_session_token', configuration.credentials.sessionToken)

        with open(filename, 'w') as fp:
            config.write(fp)

        pass

    def __writeRegion(self, configuration):
        filename = os.path.expanduser('~/.aws/config')
        dirname = os.path.dirname(filename)

        if not os.path.exists(dirname):
            os.makedirs(dirname)

        config = configparser.ConfigParser()
        config.read(filename)

        profile = 'profile ' + configuration.profile

        if not config.has_section(profile):
            config.add_section(profile)

        config.set(profile, 'region', configuration.region)
        config.set(profile, 'output', 'json')

        with open(filename, 'w') as fp:
            config.write(fp)

        pass
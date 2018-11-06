import os

from configparser import ConfigParser

from awsgen.models.profile import Profile

class ConfigurationApp(object):

    def save(self, configuration):
        self.__writeConfiguration(configuration)


    def update(self, configuration):
        self.__updateConfiguration(configuration)


    def __writeConfiguration(self, configuration):
        filename = os.path.expanduser('~/.aws/config')
        dirname = os.path.dirname(filename)

        if not os.path.exists(dirname):
            os.makedirs(dirname)

        config = ConfigParser()
        config.read(filename)

        profile = 'profile ' + configuration.profile

        if not config.has_section(profile):
            config.add_section(profile)

        config.set(profile, 'region', configuration.region)
        config.set(profile, 'output', configuration.output)

        with open(filename, 'w') as fp:
            config.write(fp)


    def __updateConfiguration(self, configuration):
        filename = os.path.expanduser('~/.aws/config')
        dirname = os.path.dirname(filename)

        if not os.path.exists(dirname):
            os.makedirs(dirname)

        config = ConfigParser()
        config.read(filename)

        profile = 'profile ' + configuration.profile

        if config.has_section(profile):
            if configuration.region:
                config.set(profile, 'region', configuration.region)
            if configuration.output:
                config.set(profile, 'output', configuration.output)

        with open(filename, 'w') as fp:
            config.write(fp)

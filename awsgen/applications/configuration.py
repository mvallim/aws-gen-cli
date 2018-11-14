import os

from configparser import ConfigParser

class ConfigurationApp(object):

    def save(self, configuration):
        self.__writeConfiguration(configuration)


    def update(self, configuration):
        self.__updateConfiguration(configuration)


    def setActive(self, profile):
        self.__writeActiveConfiguration(profile)


    def __writeActiveConfiguration(self, profile):
        filename = os.path.expanduser('~/.aws/config')
        dirname = os.path.dirname(filename)

        if not os.path.exists(dirname):
            print('File: [' + filename + '] not found')
            return None

        config = ConfigParser()
        config.read(filename)

        if not config.has_section('profile ' + profile):
            print('Profile: [' + profile + '] not found')
            return None

        config.remove_section('default')
        config.add_section('default')

        profile = 'profile ' + profile
        
        for value in config.items(profile):
            config.set('default', value[0], value[1])

        with open(filename, 'w') as fp:
            config.write(fp)


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

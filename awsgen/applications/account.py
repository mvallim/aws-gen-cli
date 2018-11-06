import os

from configparser import ConfigParser

from awsgen.models.account import Account

class AccountApp(object):

    def save(self, account):
        self.__saveAccount(account)


    def get(self, name):
        return self.__getAccount(name)


    def __getAccount(self, name):
        filename = os.path.expanduser('~/.awsgen/config')
        dirname = os.path.dirname(filename)

        if not os.path.exists(dirname):
            os.makedirs(dirname)

        config = ConfigParser()
        config.read(filename)

        account = Account(name=name)

        if config.has_section(name):
            account.trustRoleArn = config.get(name, 'role_arn')

        return account            


    def __saveAccount(self, account):
        filename = os.path.expanduser('~/.awsgen/config')
        dirname = os.path.dirname(filename)

        if not os.path.exists(dirname):
            os.makedirs(dirname)

        config = ConfigParser()
        config.read(filename)

        if not config.has_section(account.name):
            config.add_section(account.name)

        config.set(account.name, 'role_arn', account.trustRoleArn)

        with open(filename, 'w') as fp:
            config.write(fp)

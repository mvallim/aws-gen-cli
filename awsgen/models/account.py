class Account(object):

    @property
    def name(self):
        return self.__name

    @property
    def trustRoleArn(self):
        return self.__trustRoleArn

    @property
    def activeProfile(self):
        return self.__activeProfile

    @name.setter
    def name(self, value):
        self.name = value

    @trustRoleArn.setter
    def trustRoleArn(self, value):
        self.__trustRoleArn = value

    @activeProfile.setter
    def activeProfile(self, value):
        self.__activeProfile = value

    def __init__(self, name = None, trustRoleArn = None, activeProfile = None):
        self.__name = name
        self.__trustRoleArn = trustRoleArn
        self.__activeProfile = activeProfile

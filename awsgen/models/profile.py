class Profile(object):

    @property
    def name(self):
        return self.__name

    @property
    def trustRoleArn(self):
        return self.__trustRoleArn

    @property
    def sourceProfile(self):
        return self.__sourceProfile

    @property
    def credentials(self):
        return self.__credentials

    @name.setter
    def name(self, value):
        self.name = value

    @trustRoleArn.setter
    def trustRoleArn(self, value):
        self.__trustRoleArn = value

    @sourceProfile.setter
    def sourceProfile(self, value):
        self.__sourceProfile = value        

    @credentials.setter
    def credentials(self, value):
        self.__credentials = value

    def __init__(self, name = None, trustRoleArn = None, sourceProfile = None, credentials = None):
        self.__name = name
        self.__trustRoleArn = trustRoleArn
        self.__sourceProfile = sourceProfile
        self.__credentials = credentials

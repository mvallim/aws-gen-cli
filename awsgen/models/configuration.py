class Configuration(object):

    @property
    def profile(self):
        return self.__profile

    @property
    def cloudFormationRoleArn(self):
        return self.__cloudformationRoleArn

    @property
    def region(self):
        return self.__region

    @property
    def credentials(self):
        return self.__credentials

    @profile.setter
    def profile(self, value):
        self.__profile = value

    @cloudformationRoleArn.setter
    def cloudformationRoleArn(self, value):
        self.__cloudformationRoleArn = value        

    @region.setter
    def region(self, value):
        self.__region = value

    @credentials.setter
    def credentials(self, value):
        self.__credentials = value

    def __init__(self, profile = None, cloudformatiionRoleArn = None, region = None, credentials = None):
        self.__profile = profile
        self.__cloudformationRoleArn = cloudformatiionRoleArn
        self.__region = region
        self.__credentials = credentials
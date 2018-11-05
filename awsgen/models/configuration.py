class Configuration(object):

    @property
    def profile(self):
        return self.__profile

    @property
    def region(self):
        return self.__region

    @property
    def credentials(self):
        return self.__credentials

    @profile.setter
    def profile(self, value):
        self.__profile = value

    @region.setter
    def region(self, value):
        self.__region = value

    @credentials.setter
    def credentials(self, value):
        self.__credentials = value

    def __init__(self, profile = None, region = None, credentials = None):
        self.__profile = profile
        self.__region = region
        self.__credentials = credentials
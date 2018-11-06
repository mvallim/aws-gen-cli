class Request(object):

    @property
    def sourceProfile(self):
        return self.__sourceProfile

    @property
    def profile(self):
        return self.__profile

    @property
    def region(self):
        return self.__region

    @property
    def output(self):
        return self.__output        

    @sourceProfile.setter
    def sourceProfile(self, value):
        self.__sourceProfile = value

    @profile.setter
    def profile(self, value):
        self.__profile = value

    @region.setter
    def region(self, value):
        self.__region = value

    @output.setter
    def output(self, value):
        self.__output = value

    def __init__(self, profile = None, sourceProfile = None, region = None, output = None):
        self.__sourceProfile = sourceProfile
        self.__profile = profile
        self.__region = region
        self.__output = output
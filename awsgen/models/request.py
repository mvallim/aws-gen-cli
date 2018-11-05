class Request(object):

    @property
    def roleArn(self):
        return self.__roleArn

    @property
    def sessionName(self):
        return self.__sessionName

    @property
    def profileName(self):
        return self.__profileName

    @roleArn.setter
    def roleArn(self, value):
        self.__roleArn = value

    @sessionName.setter
    def sessionName(self, value):
        self.__sessionName = value

    @profileName.setter
    def profileName(self, value):
        self.__profileName = value

    def __init__(self, roleArn = None, sessionName = None, profileName = None):
        self.__roleArn = roleArn
        self.__sessionName = sessionName
        self.__profileName = profileName
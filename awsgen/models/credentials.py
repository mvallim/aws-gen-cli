class Credentials(object):

    @property
    def accessKeyId(self):
        return self.__accessKeyId

    @property
    def secretAccessKey(self):
        return self.__secretAccessKey

    @property
    def sessionToken(self):
        return self.__sessionToken

    @accessKeyId.setter
    def accessKeyId(self, value):
        self.__accessKeyId = value

    @secretAccessKey.setter
    def secretAccessKey(self, value):
        self.__secretAccessKey = value

    @sessionToken.setter
    def sessionToken(self, value):
        self.__sessionToken = value

    def __init__(self, accessKeyId = None, secretAccessKey = None, sessionToken = None):
        self.__accessKeyId = accessKeyId
        self.__secretAccessKey = secretAccessKey
        self.__sessionToken = sessionToken

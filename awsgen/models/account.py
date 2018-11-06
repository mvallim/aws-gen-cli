class Account(object):

    @property
    def name(self):
        return self.__name

    @property
    def trustRoleArn(self):
        return self.__trustRoleArn

    @name.setter
    def name(self, value):
        self.name = value

    @trustRoleArn.setter
    def trustRoleArn(self, value):
        self.__trustRoleArn = value

    def __init__(self, name = None, trustRoleArn = None):
        self.__name = name
        self.__trustRoleArn = trustRoleArn

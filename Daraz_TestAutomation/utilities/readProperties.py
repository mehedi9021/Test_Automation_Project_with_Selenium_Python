import configparser

config = configparser.RawConfigParser()
config.read(".\\configurations\\config.ini")

class ReadProperties:
    @staticmethod
    def getApplicationURL():
        url = config.get('common info','baseURL')
        return url

    @staticmethod
    def getUserPhone():
        userphone = config.get('common info','userphone')
        return userphone

    @staticmethod
    def getPassword():
        password = config.get('common info','password')
        return password
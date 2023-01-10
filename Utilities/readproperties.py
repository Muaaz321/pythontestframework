import configparser

config=configparser.RawConfigParser()
config.read(".\\Configuration\\config.ini")

class readConfig():

    @staticmethod
    def getApplicationurl():
        url=config.get('common info','baseUrl')
        return url

    @staticmethod
    def getUsername():
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password


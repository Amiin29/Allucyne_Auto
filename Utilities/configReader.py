from configparser import ConfigParser


# la fonction readConfig permet de lire le continue de ficher "conf.ini"
def readConfig(section, key):
    config = ConfigParser()
    config.read("..\\ConfigurationData\\conf.ini")
    return config.get(section, key)

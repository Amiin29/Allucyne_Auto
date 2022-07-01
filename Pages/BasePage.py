import logging

from selenium.webdriver.common.by import By
from Utilities import configReader
from Utilities.LogUtil import Logger

log = Logger(__name__, logging.INFO)


class Base:
    def __init__(self, driver):
        self.driver = driver

    # La fonction Type : c'est pour les champs a ecrire , contient les locators de type "XPATH" OU BIEN "ID"
    def type(self, locator, value):
        if str(locator).endswith("_XPATH"):
            # readConfig : c'est un appel au fonction de la classe "configReader" === va appeler au ficher conf.ini
            self.driver.find_element(By.XPATH, configReader.readConfig("locators", locator)).send_keys(value)
            log.logger.info("typing on an element : " + str(locator) + " value entered as : " + str(value))
        elif str(locator).endswith("_ID"):
            self.driver.find_element(By.ID, configReader.readConfig("locators", locator)).send_keys(value)

    # La fonction Type : c'est pour les bouttons ou les zones a cliquer , contient les locators de type "XPATH" OU
    # BIEN "ID"
    def click(self, locator):
        if str(locator).endswith("_XPATH"):
            self.driver.find_element(By.XPATH, configReader.readConfig("locators", locator)).click()
        elif str(locator).endswith("_ID"):
            self.driver.find_element(By.ID, configReader.readConfig("locators", locator)).click()

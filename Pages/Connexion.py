from selenium.webdriver.common.by import By
from Utilities import configReader
from Pages.BasePage import Base


class Connexion(Base):
    def __init__(self, driver):
        super().__init__(driver)

    def remplir_champs(self, username, password):
        self.type("username", username)
        self.type("password", password)
        self.click("Submit")


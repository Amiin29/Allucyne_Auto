import logging
import pytest
from Pages.Ajout_User import Ajout_User
from TestCases.BaseTest import BaseTest
from Utilities import dataProvider
from Utilities.LogUtil import Logger
import allure
log = Logger(__name__, logging.INFO)


# extend de la classe BaseTest
class Test_Login(BaseTest):

    @pytest.mark.parametrize("username, password", dataProvider.get_data("LoginTest"))
    # extend de la focntion get data de la classe data_provider
    # (LoginTest = c'est le nom de classeur du fichier excel)
    def test_dologin(self, username, password):
        log.logger.info("Test Do login started")
        regPage = Ajout_User(self.driver)
        # appel au l'instructeur Ajout_user de la classe Ajout_User et envoie en paramètre le driver
        regPage.remplir_champs_ajout_user(username, password)
        # appel au fonction remplir_champs_ajout_user de la classe Ajout User et envoie en paramètre username , password
        log.logger.info("Test Do login finished")

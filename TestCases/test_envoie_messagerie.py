import logging
import pytest
from Pages.Ajout_User import Ajout_User
from Pages.Envoie_Messagerie import Envoie_Messagerie
from TestCases.BaseTest import BaseTest
from Utilities import dataProvider
from Utilities.LogUtil import Logger

log = Logger(__name__, logging.INFO)


# extend de la classe BaseTest
class Test_envoie_messagerie(BaseTest):
    @pytest.mark.parametrize("username, password", dataProvider.get_data("LoginTest"))
    def test_dologin(self, username, password):
        log.logger.info("Test Do login started")
        regPage = Envoie_Messagerie(self.driver)
        regPage.Connexion(username, password)
        regPage.Envoie_Messagerie()
        log.logger.info("Test Do login finished")

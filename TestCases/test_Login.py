import logging

import openpyxl
import pytest

from Pages.Ajout_User import Ajout_User
from Pages.BasePage import Base
from Pages.Connexion import Connexion
from TestCases.BaseTest import BaseTest
from Utilities import dataProvider
from Utilities.LogUtil import Logger

log = Logger(__name__, logging.INFO)


class Test_Login(BaseTest):

    @pytest.mark.parametrize("username, password", dataProvider.get_data("LoginTest"))
    def test_dologin(self, username, password):
        log.logger.info("Test Do login started")
        regPage = Ajout_User(self.driver)
        regPage.remplir_champs_ajout_user(username, password)
        log.logger.info("Test Do login finished")


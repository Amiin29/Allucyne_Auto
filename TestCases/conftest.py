from selenium import webdriver
import pytest
from Utilities import configReader


# c'est une classe qu'on peut la définir une seul fois dans chaque fichier pour faire la configuration de chrome
# driver et l'URL

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture()
def log_on_failure(request, get_browser):
    yield
    item = request.node
    driver = get_browser


@pytest.fixture(params=["chrome"], scope="function")
def get_browser(request):
    # Le chemin de Chrome driver dans mon PC
    driver = webdriver.Chrome(executable_path='C:\\Users\\Asus\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe')
    request.cls.driver = driver
    # Appel au fonction readConfig pour passer en parametre le section et l'URL de Allucyne
    driver.get(configReader.readConfig("basic info", "testsiteurl"))
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver

import time
from selenium.webdriver.common.by import By
from Pages.BasePage import Base


# ------------------------Constructeur parametré de la classe Ajout_User------------
class Envoie_Messagerie(Base):
    def __init__(self, driver):
        super().__init__(driver)

    # ---------------------- fonction remplir_champs_ajout_user--------------------------------------------
    def Connexion(self, username, password):
        # --------------------------les attributs  username et password d'après le ficier "Excel"
        time.sleep(1.0)
        self.type("username_ID", username)
        time.sleep(1.0)
        self.type("password_ID", password)
        time.sleep(1.0)
        self.click("Submit_ID")

    def Envoie_Messagerie(self):
        time.sleep(1.0)
        self.click("custom_card_XPATH")
        time.sleep(1.5)
        self.click("Message_personels_XPATH")
        time.sleep(1.5)
        self.click("click_XPATH")
        time.sleep(1.5)
        self.click("click_2_XPATH")
        time.sleep(2.0)
        self.driver.find_element(By.XPATH,
                                 "//div[@class='position-relative']//textarea[@placeholder='Écrire un message']").send_keys(
            "Hellooooo Amin from script automated ")
        # Cliquer sur le bouton Envoie
        self.click("envoie_ms_XPATH")
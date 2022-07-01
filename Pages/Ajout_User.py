import time
from selenium.webdriver.common.by import By
from Pages.BasePage import Base


# ------------------------Constructeur parametré de la classe Ajout_User------------
class Ajout_User(Base):
    def __init__(self, driver):
        super().__init__(driver)

    # ---------------------- fonction remplir_champs_ajout_user--------------------------------------------
    def remplir_champs_ajout_user(self, username, password):
        # --------------------------les attributs  username et password d'après le ficier "Excel"
        time.sleep(1.0)
        self.type("username_ID", username)
        time.sleep(1.0)
        self.type("password_ID", password)
        time.sleep(1.0)
        self.click("Submit_ID")
        time.sleep(1.0)
        self.click("custom_card_XPATH")
        time.sleep(1.0)
        self.click("Administration_du_site_XPATH")
        time.sleep(1.5)
        self.click("Ajouter_un_utilisateur_XPATH")
        time.sleep(1.5)
        # ---------------------------Remplir les champs de la page ajout User-------------------------------
        self.driver.find_element(By.ID, "id_username").send_keys("amin29")
        time.sleep(1.0)
        self.driver.find_element(By.XPATH, "//input[@id='id_createpassword']").click()
        self.driver.find_element(By.XPATH, "//input[@id='id_profile_field_code_etudiant']").send_keys("KFKD6")
        time.sleep(1.0)
        self.driver.find_element(By.XPATH, "//input[@id='id_profile_field_nom_marital']").send_keys("MDJS")
        time.sleep(1.0)
        self.driver.find_element(By.XPATH, "//input[@id='id_profile_field_code_diplome']").send_keys("MDJS")
        time.sleep(1.0)
        self.driver.find_element(By.ID, "id_firstname").send_keys("Amin")
        time.sleep(1.0)
        self.driver.find_element(By.ID, "id_lastname").send_keys("Miladi")
        time.sleep(1.0)
        self.driver.find_element(By.ID, "id_email").send_keys("amin29.miladi@gmail.com")
        time.sleep(1.0)
        self.driver.find_element(By.ID, "id_submitbutton").click()

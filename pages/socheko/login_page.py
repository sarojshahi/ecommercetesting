#IMPORT ALL THE NECESSARY MODULES
from selenium.webdriver.common.by import By

#DEFINE CLASS FOR LOGIN PAGE OF SOCHEKO

class LoginPageSocheko:
    def __init__(self,driver):
        self.driver = driver
        self.userid_field = By.XPATH,"//input[@name='id']"
        self.password_field = By.XPATH,"//input[@name='password']"
        self.login_button = By.XPATH,"//button[normalize-space()='Login']"

    def open_page(self,url):
        self.driver.get(url)

    def enter_userid(self, userid):
        self.driver.find_element(*self.userid_field).send_keys(userid)

    def enter_password(self,password):
        self.driver.find_element(*self.password_field).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()


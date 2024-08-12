#IMPORT ALL THE NECESSARY MODULES
from selenium.webdriver.common.by import By

#DEFINE CLASS FOR LOGIN PAGE OF GOLDSTAR
class LoginPageGoldstar:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = By.XPATH,"//input[@id='txtUserName']"
        self.password_field = By.XPATH,"//input[@id='txtUserPassword']"
        self.login_button = By.XPATH,"//button[@id='btnSignIn']"
    def open_page(self,url):
        self.driver.get(url)

    def enter_username(self, username):
        self.driver.find_element(*self.username_field).send_keys(username)

    def enter_password(self, pwd):
        self.driver.find_element(*self.password_field).send_keys(pwd)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()


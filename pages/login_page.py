#IMPORT ALL THE NECESSARY MODULES
from selenium.webdriver.common.by import By
import time

#DEFINE CLASS AS Login FOR THE LOGIN PAGE
class LoginPage:
    def __init__(self,driver):
        self.driver = driver
        self.user_id_field = By.XPATH,"//input[@id='email']"
        self.user_password_field = By.XPATH,"//fieldset[@class='fieldset login']//input[@id='pass']"
        self.login_button = By.XPATH,"//fieldset[@class='fieldset login']//button[@id='send2']"

    def open_page(self,url):
        self.driver.get(url)

    def enter_userid(self,userid):
        self.driver.find_element(*self.user_id_field).send_keys(userid)

    def enter_user_password(self,password):
        self.driver.find_element(*self.user_password_field).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()


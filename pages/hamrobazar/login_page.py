#IMPORT ALL THE NECESSARY MODULES
from selenium.webdriver.common.by import By

#DEFINE CLASS FOR LOGIN PAGE OF HAMROBAZAR
class LoginPageHB:
    def __init__(self, driver):
        self.driver = driver
        self.phone_field = By.XPATH,"//input[@placeholder='Phone Number']"
        self.password_field = By.XPATH,"//input[@placeholder='Password']"
        self.login_button = By.XPATH,"//button[normalize-space()='Log In']"
    def open_page(self,url):
        self.driver.get(url)

    def enter_phonenumber(self, phone):
        self.driver.find_element(*self.phone_field).send_keys(phone)

    def enter_password(self, pwd):
        self.driver.find_element(*self.password_field).send_keys(pwd)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()


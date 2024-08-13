#IMPORT ALL THE NECESSARY MODULES
from selenium.webdriver.common.by import By

#DEFINE CLASS FOR LOGIN PAGE OF SALT NEPAL

class LoginPageSalt:
    def __init__(self,driver):
        self.driver = driver
        self.useremail_field = By.XPATH,"//input[@id='customer_email']"
        self.password_field = By.XPATH,"//input[@id='customer_password']"
        self.signin_button = By.XPATH,"//input[@value='Sign In']"

    def open_page(self,url):
        self.driver.get(url)

    def enter_useremail(self, useremail):
        self.driver.find_element(*self.useremail_field).send_keys(useremail)

    def enter_password(self,password):
        self.driver.find_element(*self.password_field).send_keys(password)

    def click_signin(self):
        self.driver.find_element(*self.signin_button).click()


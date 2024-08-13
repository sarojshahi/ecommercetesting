#IMPORT ALL THE NECESSARY MODULES
from selenium.webdriver.common.by import By
import re

#DEFINE CLASS FOR REGISTRATION PAGE OF SALT NEPAL

class RegistrationPageSalt:
    def __init__(self,driver):
        self.driver = driver
        self.first_name_field = By.XPATH,"//input[@id='first_name']"
        self.last_name_field = By.XPATH,"//input[@id='last_name']"
        self.email_field= By.XPATH,"//input[@id='email']"
        self.password_field = By.XPATH,"//input[@id='password']"
        self.create_button = By.XPATH,"//input[@value='Create']"

    def open_page(self,url):
        self.driver.get(url)

    def enter_first_name(self,firstname):
        self.driver.find_element(*self.first_name_field).send_keys(firstname)

    def enter_last_name(self,lastname):
        self.driver.find_element(*self.last_name_field).send_keys(lastname)

    def enter_email(self,email):
        self.driver.find_element(*self.email_field).send_keys(email)

    def enter_password(self,password):
        self.driver.find_element(*self.password_field).send_keys(password)

    def click_create(self):
        self.driver.find_element(*self.create_button).click()

    def is_valid_email(self, email):
        # check the format using Regular Expression(re)
        email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return re.match(email_regex, email) is not None
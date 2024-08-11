#IMPORT ALL THE NECESSARY MODULES
from selenium.webdriver.common.by import By
import re

#DEFINE CLASS AS Registration FOR REGISTRATION PAGE
class RegistrationPageOliz:
    def __init__(self,driver):
        self.driver = driver
        self.firstname_field = By.XPATH,"//input[@id='firstname']"
        self.last_name_field = By.XPATH,"//input[@id='lastname']"
        self.email_field = By.XPATH,"//input[@id='email_address']"
        self.password_field = By.XPATH,"//input[@id='password']"
        self.confirm_password_field = By.XPATH,"//input[@id='password-confirmation']"
        self.create_button = By.XPATH,"//button[@title='Create an Account']"


    def open_page(self,url):
        self.driver.get(url)
    def enter_firstname(self,firstname):
        self.driver.find_element(*self.firstname_field).send_keys(firstname)

    def enter_lastname(self, lastname):
        self.driver.find_element(*self.last_name_field).send_keys(lastname)

    def enter_email(self, email):
        self.driver.find_element(*self.email_field).send_keys(email)

    def enter_password(self,password):
        self.driver.find_element(*self.password_field).send_keys(password)

    def enter_confirm_password(self,confirm_password):
        self.driver.find_element(*self.confirm_password_field).send_keys(confirm_password)

    def click_create_button(self):
        self.driver.find_element(*self.create_button).click()

    def is_valid_email(self, email):
        # check the format using Regular Expression(re)
        email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return re.match(email_regex, email) is not None
    def is_valid_phone(self, phone):
        return bool(re.match(r'^\d{10}$', phone))
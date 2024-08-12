#IMPORT ALL THE NECESSARY MODULES
from selenium.webdriver.common.by import By
import re

#DEFINE CLASS FOR REGISTRATION PAGE OF GOLDSTAR
class RegistrationPageGoldstar:
    def __init__(self,driver):
        self.driver = driver
        self.first_name_field = By.XPATH,"//input[contains(@name,'FirstName')]"
        self.last_name_field = By.XPATH,"//input[@name='LastName']"
        self.email_field= By.XPATH,"//input[@id='txtRegUserEmail']"
        self.password_field = By.XPATH,"//input[@id='txtRegUserPassword']"
        self.confirm_password_field = By.XPATH,"//input[@id='txtRegConfirmpassword']"
        self.register_button = By.XPATH,"//button[@id='btnRegCreateUser']"

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

    def enter_confirm_password(self, confirm_password):
        self.driver.find_element(*self.confirm_password_field).send_keys(confirm_password)

    def click_register(self):
        self.driver.find_element(*self.register_button).click()

    def is_valid_email(self, email):
        # check the format using Regular Expression(re)
        email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return re.match(email_regex, email) is not None
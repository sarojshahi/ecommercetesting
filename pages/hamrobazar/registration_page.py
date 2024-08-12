#IMPORT ALL THE NECESSARY MODULES
from selenium.webdriver.common.by import By
import re

#DEFINE CLASS FOR REGISTRATION PAGE OF HAMROBAZAR
class RegistrationPageHB:
    def __init__(self, driver):
        self.driver = driver
        self.fullname_field = By.XPATH,"//input[@placeholder='Full Name']"
        self.phone_field = By.XPATH,"//input[@placeholder='Phone Number']"
        self.password_field = By.XPATH,"//input[@placeholder='Password']"
        self.terms_checklist = By.XPATH,"//label[@for='accept']"
        self.sign_up_button = By.XPATH,"//button[@type='submit'][normalize-space()='Sign Up']"
    def open_page(self,url):
        self.driver.get(url)

    def enter_fullname(self, fullname):
        self.driver.find_element(*self.fullname_field).send_keys(fullname)

    def enter_phone(self, phone):
        self.driver.find_element(*self.phone_field).send_keys(phone)

    def enter_password(self, password):
        self.driver.find_element(*self.password_field).send_keys(password)

    def click_accept(self):
        self.driver.find_element(*self.terms_checklist).click()

    def click_signup(self):
        self.driver.find_element(*self.sign_up_button).click()

    def is_valid_phone(self, phone):
        return bool(re.match(r'^\d{10}$', phone))
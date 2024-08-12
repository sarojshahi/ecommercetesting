#IMPORT ALL THE NECESSARY MODULES
from selenium.webdriver.common.by import By
import re
from selenium.webdriver.support.ui import Select

#DEFINE CLASS AS Registration FOR REGISTRATION PAGE OF MUNCHA

class RegistrationPageMuncha:
    def __init__(self,driver):
        self.driver = driver
        self.full_name_field = By.XPATH,"//input[@id='Name']"
        self.email_field = By.XPATH,"//input[@id='Email']"
        self.contact_field = By.XPATH,"//input[@id='ContactNo']"
        self.password_field = By.XPATH,"//input[@id='Password']"
        self.confirm_password_field = By.XPATH,"//input[@id='ConfirmPassword']"
        self.hear_about_us_field = (By.ID,'Referer')
        self.newsletter_checklist = By.XPATH,"//input[@id='accept-email']"
        self.sign_up_button = By.XPATH,"//button[@title='Create an Account']"


    def open_page(self,url):
        self.driver.get(url)
    def enter_fullname(self,fullname):
        self.driver.find_element(*self.full_name_field).send_keys(fullname)

    def enter_email(self, email):
        self.driver.find_element(*self.email_field).send_keys(email)

    def enter_contact(self, contact):
        self.driver.find_element(*self.contact_field).send_keys(contact)

    def enter_password(self,password):
        self.driver.find_element(*self.password_field).send_keys(password)

    def enter_confirm_password(self,confirm_password):
        self.driver.find_element(*self.confirm_password_field).send_keys(confirm_password)

    def click_hearabout(self):
        referer_dropdown = self.driver.find_element(*self.hear_about_us_field)
        select = Select(referer_dropdown)
        select.select_by_index(1)


    def click_newsletter(self):
        self.driver.find_element(*self.newsletter_checklist).click()

    def click_signup(self):
        self.driver.find_element(*self.sign_up_button).click()

    def is_valid_email(self, email):
        # check the format using Regular Expression(re)
        email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return re.match(email_regex, email) is not None
    def is_valid_phone(self, phone):
        return bool(re.match(r'^\d{10}$', phone))
#IMPORT ALL THE NECESSARY MODULES
from selenium.webdriver.common.by import By

#DEFINE CLASS FOR REGISTRATION PAGE OF KHALTI PAGE
class RegistrationPageKhalti:
    def __init__(self,driver):
        self.driver = driver
        self.fullname_field = By.XPATH,"//input[@name='name']"
        self.mobile_number_field = By.XPATH,"//input[@placeholder='Mobile number']"
        self.email_field = By.XPATH,"//input[@type='email']"
        self.dob_field = By.XPATH,"//input[@name='dob']"
        self.male_gender_checklist = By.XPATH,"//label[normalize-space()='Male']"
        self.password_field = By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[3]/div[1]/form[1]/div[6]/div[1]/div[1]/div[2]/input[1]"
        self.confirm_password_field = By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[3]/div[1]/form[1]/div[7]/div[1]/div[1]/div[2]/input[1]"
        self.join_button = By.XPATH,"//button[normalize-space()='Join']"

    def open_page(self,url):
        self.driver.get(url)

    def enter_fullname(self,fullname):
        self.driver.find_element(*self.fullname_field).send_keys(fullname)

    def enter_mobile(self,mobile):
        self.driver.find_element(*self.mobile_number_field).send_keys(mobile)


    def enter_email(self,email):
        self.driver.find_element(*self.email_field).send_keys(email)

    def enter_dob(self, dob):
        self.driver.find_element(*self.dob_field).send_keys(dob)

    def enter_gender(self):
        self.driver.find_element(*self.male_gender_checklist).click()

    def enter_password(self,password):
        self.driver.find_element(*self.password_field).send_keys(password)

    def enter_confirm_password(self,confirm_password):
        self.driver.find_element(*self.confirm_password_field).send_keys(confirm_password)

    def click_join(self):
        self.driver.find_element(*self.join_button).click()
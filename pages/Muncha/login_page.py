#IMPORT ALL THE NECESSARY MODULES
from selenium.webdriver.common.by import By

#DEFINE CLASS AS Login FOR THE LOGIN PAGE OF MUNCHA
class LoginPageMuncha:
    def __init__(self,driver):
        self.driver = driver
        self.email_field = By.XPATH,"//input[@id='Username']"
        self.user_password_field = By.XPATH,"//input[@id='Password']"
        self.signup_button = By.XPATH,"//button[@class='bg-secondary border border-gray-400 px-4 py-2.5 text-md w-full text-white']"

    def open_page(self,url):
        self.driver.get(url)

    def enter_userid(self,email_id):
        self.driver.find_element(*self.email_field).send_keys(email_id)

    def enter_user_password(self,password):
        self.driver.find_element(*self.user_password_field).send_keys(password)

    def click_signup(self):
        self.driver.find_element(*self.signup_button).click()


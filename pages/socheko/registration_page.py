#IMPORT ALL THE NECESSARY MODULES
from selenium.webdriver.common.by import By

#DEFINE CLASS FOR REGISTRATION PAGE OF SOCHEKO PAGE
class RegistrationPageSocheko:
    def __init__(self,driver):
        self.driver = driver
        self.email_field= By.XPATH,"//div[@class='flex flex-wrap']//input[@id='grid-name']"
        self.name_field = By.XPATH,"//body/div[@id='app']/div[@class='text-sm']/div[@class='lg:grid grid-cols-1 min-h-screen']/main[@class='flex flex-col']/div[@class='flex-1']/div[@class='bg-gray-50 lg:py-10 h-full']/div[@class='container mx-auto']/div[@class='p-4 lg:p-10 max-w-lg lg:shadow-xl bg-white mx-auto border border-white rounded-xl overflow-hidden loginBg-right']/div[@class='w-full pb-4']/input[1]"
        self.password_field = By.XPATH,"//input[@id='Password']"
        self.confirm_password_field = By.XPATH,"//input[@id='Confirm_Password']"
        self.register_button = By.XPATH,"//button[@type='button'][normalize-space()='Register']"

    def open_page(self,url):
        self.driver.get(url)

    def enter_email(self,email):
        self.driver.find_element(*self.email_field).send_keys(email)

    def enter_name(self,name):
        self.driver.find_element(*self.name_field).send_keys(name)

    def enter_password(self,password):
        self.driver.find_element(*self.password_field).send_keys(password)

    def enter_confirm_password(self, confirm_password):
        self.driver.find_element(*self.confirm_password_field).send_keys(confirm_password)

    def click_register(self):
        self.driver.find_element(*self.register_button).click()
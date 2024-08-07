#IMPORT ALL THE NECESSARY MODULES
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import time

#IMPORT THE CLASSES FROM THE PAGES
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage



@pytest.fixture()
def driver():
    #SETTING UP THE CHROME DRIVER MANAGER AS driver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(2)
    #YIELD THE DRIVER
    yield driver
    #CLOSE THE DRIVER INSTANCE
    driver.quit()

@pytest.mark.parametrize("useremail,userpassword",[
    ("andromedanp.hq@gmail.com","Tumblr@123"),
    ("ram@gmail.com","abc123"),
    ("9810110101","helloworld101")
])

def test_login(driver, useremail,userpassword):
    login = LoginPage(driver)
    login.open_page('https://www.olizstore.com/customer/account/login/')
    driver.maximize_window()
    time.sleep(2)
    login.enter_userid(useremail)
    time.sleep(1)
    login.enter_user_password(userpassword)
    time.sleep(1)
    login.click_login()
    time.sleep(3)

def test_registration(driver):
    registration = RegistrationPage(driver)
    registration.open_page("https://www.olizstore.com/customer/account/create/")
    driver.maximize_window()
    time.sleep(2)
    registration.enter_firstname("Ram")
    time.sleep(1)
    registration.enter_lastname("Nepali")
    time.sleep(1)
    registration.enter_email("ram@gmail.com")
    time.sleep(1)
    registration.enter_password("123456")
    time.sleep(1)
    registration.enter_confirm_password("123456")
    time.sleep(1)
    registration.click_create_button()
    time.sleep(3)






#IMPORT ALL THE NECESSARY MODULES
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import time

#IMPORT THE CLASSES FROM THE PAGES
from pages.olizstore.login_page import LoginPage
from pages.olizstore.registration_page import RegistrationPage
from pages.khalti.registration_page import RegistrationPage

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

#RUNNING TEST FUNCTION ON OLIZ LOGIN PAGE
def test_login_oliz(driver, useremail,userpassword):
    oliz_login = LoginPage(driver)
    oliz_login.open_page('https://www.olizstore.com/customer/account/login/')
    driver.maximize_window()
    time.sleep(2)
    oliz_login.enter_userid(useremail)
    time.sleep(1)
    oliz_login.enter_user_password(userpassword)
    time.sleep(1)
    oliz_login.click_login()
    time.sleep(3)


#RUNNING TEST FUNCTION ON OLIZ REGISTRATION PAGE
def test_registration_oliz(driver):
    oliz_registration = RegistrationPage(driver)
    oliz_registration.open_page("https://www.olizstore.com/customer/account/create/")
    driver.maximize_window()
    time.sleep(2)
    oliz_registration.enter_firstname("Ram")
    time.sleep(1)
    oliz_registration.enter_lastname("Nepali")
    time.sleep(1)
    oliz_registration.enter_email("ram@gmail.com")
    time.sleep(1)
    oliz_registration.enter_password("123456")
    time.sleep(1)
    oliz_registration.enter_confirm_password("123456")
    time.sleep(1)
    oliz_registration.click_create_button()
    time.sleep(3)


####################################################################

#RUNNING TEST FUNCTION ON KHALTI REGISTRATION PAGE
def test_registration_khalti(driver):
    khalti_registration = RegistrationPage(driver)
    khalti_registration.open_page("https://web.khalti.com/?csrt=5394820902130000854#/join")
    driver.maximize_window()
    time.sleep(1)
    khalti_registration.enter_fullname("Ram Nepali")
    time.sleep(1)
    khalti_registration.enter_mobile("9")
    time.sleep(1)
    khalti_registration.enter_email("ram@gmail.com")
    time.sleep(1)
    khalti_registration.enter_dob("1990/01/01")
    time.sleep(1)
    khalti_registration.enter_gender()
    time.sleep(1)
    khalti_registration.enter_password("dummy123")
    time.sleep(1)
    khalti_registration.enter_confirm_password("dummy123")
    time.sleep(1)
    khalti_registration.click_join()
    time.sleep(5)


def test_login_khalti(driver):
    khalti_login = LoginPage(driver)
    khalti_login.open_page("https://web.khalti.com/?csrt=5394820902130000854#/")
    driver.maximize_window()
    time.sleep(1)
    khalti_login.enter_userid("ram@gmail.com")
    time.sleep(1)
    khalti_login.enter_user_password("tumblr@123")
    time.sleep(1)
    khalti_login.click_login()
    time.sleep(3)




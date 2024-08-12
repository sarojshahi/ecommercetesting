#IMPORT ALL THE NECESSARY MODULES
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import time

#IMPORT THE CLASSES FROM THE PAGES
from pages.Muncha.registration_page import RegistrationPageMuncha
from pages.Muncha.login_page import LoginPageMuncha
from pages.socheko.login_page import LoginPageSocheko
from pages.goldstar.registration_page import RegistrationPageGoldstar
from pages.goldstar.login_page import  LoginPageGoldstar


@pytest.fixture()
def driver():
    #SETTING UP THE CHROME DRIVER MANAGER AS driver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(2)
    #YIELD THE DRIVER
    yield driver
    #CLOSE THE DRIVER INSTANCE
    driver.quit()



#RUNNING TEST FUNCTION ON HAMROBAZAR REGISTRATION PAGE
def test_registration_goldstar(driver):
    email = "johndoe01@gmail.com"
    goldstar_registration = RegistrationPageGoldstar(driver)
    goldstar_registration.open_page("https://www.goldstarshoes.com/register")
    driver.maximize_window()
    time.sleep(1)
    goldstar_registration.enter_first_name("John")
    time.sleep(1)
    goldstar_registration.enter_last_name("Doe")
    time.sleep(1)
    goldstar_registration.enter_email(email)
    time.sleep(1)
    goldstar_registration.enter_password("Nepali@123")
    time.sleep(1)
    goldstar_registration.enter_confirm_password("Nepali@123")
    time.sleep(1)
    # goldstar_registration.click_register()
    # time.sleep(1)

    # check the validity of the email
    if goldstar_registration.is_valid_email(email):
        print(f"The given email: {email} is valid")
    else:
        print(f"The given email: {email} is invalid")


#Testing the different login credentials using Parameterization of GOLDSTAR
@pytest.mark.parametrize("useremail,userpassword",[
    ("johndoe01@gmail.com","Nepali@123"),
    ("johndoe01@gmail.com","nepali@@123"),
    ("johndai@gmail.com","Nepali@123"),
    ("","")
])
def test_login_goldstar(driver, useremail,userpassword):
    goldstar_login = LoginPageGoldstar(driver)
    goldstar_login.open_page("https://www.goldstarshoes.com/login")
    driver.maximize_window()
    time.sleep(1)
    goldstar_login.enter_username(useremail)
    time.sleep(1)
    goldstar_login.enter_password(userpassword)
    time.sleep(1)
    goldstar_login.click_login()
    time.sleep(3)


#RUNNING TEST FUNCTION ON OLIZ REGISTRATION PAGE

def test_registration_muncha(driver):
    email = "johndoe@gmail.com"
    phone = "9810120230"
    muncha_registration = RegistrationPageMuncha(driver)
    muncha_registration.open_page("https://www.muncha.com/AP/Register")
    driver.maximize_window()
    time.sleep(2)
    muncha_registration.enter_fullname("John Doe")
    time.sleep(1)
    muncha_registration.enter_email(email)
    time.sleep(1)
    muncha_registration.enter_contact(phone)
    time.sleep(1)
    muncha_registration.enter_password("Nepali@123")
    time.sleep(1)
    muncha_registration.enter_confirm_password("Nepali@123")
    time.sleep(1)
    muncha_registration.click_hearabout()
    time.sleep(1)
    muncha_registration.click_newsletter()
    time.sleep(1)
    # muncha_registration.click_signup()
    # time.sleep(3)
    # check the validity of the email
    if muncha_registration.is_valid_email(email):
        print(f"The given email: {email} is valid")
    else:
        print(f"The given email: {email} is invalid")


    # check the validity of the email
    if muncha_registration.is_valid_phone(phone):
        print(f"The given email: {phone} is valid")
    else:
        print(f"The given email: {phone} is invalid")

#TESTING DIFFERENT LOGIN CREDENTIALS USING PARAMETERIZATION
@pytest.mark.parametrize("useremail,userpassword",[
    ("johndoe@gmail.com","Nepali@123"),
    ("johndoe@gmail.com","nepali@@123"),
    ("johndai@gmail.com","Nepali@123"),
    ("","")
])

#RUNNING TEST FUNCTION ON OLIZ LOGIN PAGE
def test_login_muncha(driver, useremail,userpassword):
    muncha_login = LoginPageMuncha(driver)
    muncha_login.open_page("https://www.muncha.com/ap/login")
    driver.maximize_window()
    time.sleep(2)
    muncha_login.enter_userid(useremail)
    time.sleep(1)
    muncha_login.enter_user_password(userpassword)
    time.sleep(1)
    muncha_login.click_signup()
    time.sleep(3)


####################################################################

#RUNNING TEST FUNCTION ON SOCHEKO REGISTRATION PAGE
def test_registration_socheko(driver):
    email = "johndoe@gmail.com"
    socheko_registration = RegistrationPageSocheko(driver)
    socheko_registration.open_page("http://www.socheko.com/signup-user")
    driver.maximize_window()
    time.sleep(1)
    socheko_registration.enter_email(email)
    time.sleep(1)
    socheko_registration.enter_name("John Doe")
    time.sleep(1)
    socheko_registration.enter_password("Nepali@123")
    time.sleep(1)
    socheko_registration.enter_confirm_password("Nepali@123")
    time.sleep(1)
    socheko_registration.click_register()
    time.sleep(1)

    # check the validity of the email
    if socheko_registration.is_valid_email(email):
        print(f"The given email: {email} is valid")
    else:
        print(f"The given email: {email} is invalid")


#Testing the different login credentials using Parameterization
@pytest.mark.parametrize("useremail,userpassword",[
    ("andromedanp.hq@gmail.com","Tumblr@123"),
    ("ram@gmail.com","abc123"),
    ("9810110101","helloworld101")
])

#RUNNING TEST FUNCTION ON SOCHEKO REGISTRATION PAGE
def test_login_socheko(driver,useremail,userpassword):
    socheko_login = LoginPageSocheko(driver)
    socheko_login.open_page("http://www.socheko.com/login-user")
    driver.maximize_window()
    time.sleep(1)
    socheko_login.enter_userid(useremail)
    time.sleep(1)
    socheko_login.enter_password(userpassword)
    time.sleep(1)
    socheko_login.click_login()
    time.sleep(3)

#####################################################################

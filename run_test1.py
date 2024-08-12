#IMPORT ALL THE NECESSARY MODULES
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import time

#IMPORT THE CLASSES FROM THE PAGES
from pages.olizstore.registration_page import RegistrationPageOliz
from pages.olizstore.login_page import LoginPageOliz
from pages.khalti.registration_page import RegistrationPageKhalti
from pages.khalti.login_page import LoginPageKhalti
from pages.hamrobazar.registration_page import RegistrationPageHB
from pages.hamrobazar.login_page import LoginPageHB


@pytest.fixture()
def driver():
    #SETTING UP THE CHROME DRIVER MANAGER AS driver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(2)
    #YIELD THE DRIVER
    yield driver
    #CLOSE THE DRIVER INSTANCE
    driver.quit()


#RUNNING TEST FUNCTION ON OLIZ REGISTRATION PAGE

def test_registration_oliz(driver):
    email = "ram@@gmail.com"
    phone = "abc1234"
    oliz_registration = RegistrationPageOliz(driver)
    oliz_registration.open_page("https://www.olizstore.com/customer/account/create/")
    driver.maximize_window()
    time.sleep(2)
    oliz_registration.enter_firstname("Ram")
    time.sleep(1)
    oliz_registration.enter_lastname("Nepali")
    time.sleep(1)
    oliz_registration.enter_email(email)
    time.sleep(1)
    oliz_registration.enter_password("123456")
    time.sleep(1)
    oliz_registration.enter_confirm_password("123456")
    time.sleep(1)
    oliz_registration.click_create_button()
    time.sleep(3)

    # check the validity of the email
    if oliz_registration.is_valid_email(email):
        print(f"The given email: {email} is valid")
    else:
        print(f"The given email: {email} is invalid")

#TESTING DIFFERENT LOGIN CREDENTIALS USING PARAMETERIZATION
@pytest.mark.parametrize("useremail,userpassword",[
    ("andromedanp.hq@gmail.com","Tumblr@123"),
    ("ram@gmail.com","abc123"),
    ("9810110101","helloworld101")
])

#RUNNING TEST FUNCTION ON OLIZ LOGIN PAGE
def test_login_oliz(driver, useremail,userpassword):
    oliz_login = LoginPageOliz(driver)
    oliz_login.open_page('https://www.olizstore.com/customer/account/login/')
    driver.maximize_window()
    time.sleep(2)
    oliz_login.enter_userid(useremail)
    time.sleep(1)
    oliz_login.enter_user_password(userpassword)
    time.sleep(1)
    oliz_login.click_login()
    time.sleep(3)


####################################################################

#RUNNING TEST FUNCTION ON KHALTI REGISTRATION PAGE
def test_registration_khalti(driver):
    mobilenum = "923123212"
    email = "ram@@gmail.com"
    khalti_registration = RegistrationPageKhalti(driver)
    khalti_registration.open_page("https://web.khalti.com/?csrt=5394820902130000854#/join")
    driver.maximize_window()
    time.sleep(1)
    time.sleep(1)
    khalti_registration.enter_mobile(mobilenum)
    khalti_registration.enter_fullname("Ram Nepali")
    time.sleep(1)
    khalti_registration.enter_email(email)
    time.sleep(1)
    khalti_registration.enter_dob("1990/01/01")
    time.sleep(1)
    khalti_registration.enter_gender()
    time.sleep(1)
    khalti_registration.enter_password("dummy123")
    time.sleep(1)
    khalti_registration.enter_confirm_password("dummy123")
    time.sleep(1)
    # khalti_registration.click_join()
    # time.sleep(5)

    # check the validity of the email
    if khalti_registration.is_valid_email(email):
        print(f"The given email: {email} is valid")
    else:
        print(f"The given email: {email} is invalid")

    # check the validity of the phone
    if khalti_registration.is_valid_phone(mobilenum):
        print(f"The given number:{mobilenum} is valid")
    else:
        print(f"The given number:{mobilenum} is invalid")


#Testing the different login credentials using Parameterization
@pytest.mark.parametrize("useremail,userpassword",[
    ("andromedanp.hq@gmail.com","Tumblr@123"),
    ("ram@gmail.com","abc123"),
    ("9810110101","helloworld101")
])

#RUNNING TEST FUNCTION ON KHALTI REGISTRATION PAGE
def test_login_khalti(driver,useremail,userpassword):
    khalti_login = LoginPageKhalti(driver)
    khalti_login.open_page("https://web.khalti.com/?csrt=5394820902130000854#/")
    driver.maximize_window()
    time.sleep(1)
    khalti_login.enter_userid(useremail)
    time.sleep(1)
    khalti_login.enter_password(userpassword)
    time.sleep(1)
    khalti_login.click_login()
    time.sleep(3)

#####################################################################

#RUNNING TEST FUNCTION ON HAMROBAZAR REGISTRATION PAGE
def test_registration_hamrobazar(driver):
    phonenum = "9801111111"
    hamrobazar_registration = RegistrationPageHB(driver)
    hamrobazar_registration.open_page("https://hamrobazaar.com/signup")
    driver.maximize_window()
    time.sleep(1)
    hamrobazar_registration.enter_fullname("John Doe")
    time.sleep(1)
    hamrobazar_registration.enter_phone(phonenum)
    time.sleep(1)
    hamrobazar_registration.click_accept()
    time.sleep(1)
    hamrobazar_registration.click_signup()
    time.sleep(1)

    # check the validity of the phone
    if hamrobazar_registration.is_valid_phone(phonenum):
        print(f"The given number: {phonenum} is valid")
    else:
        print(f"The given number:{phonenum} is invalid")


#Testing the different login credentials using Parameterization
@pytest.mark.parametrize("userid,userpassword",[
    ("918138213","Tumblr@123"),
    ("testuser@gmail.com","Test@password123"),
    ("9810110101","a"),
    ("a","Test@passowrd123")
])
def test_login_hamrobazar(driver, userid,userpassword):
    hamrobazar_login = LoginPageHB(driver)
    hamrobazar_login.open_page("https://hamrobazaar.com/login")
    driver.maximize_window()
    time.sleep(1)
    hamrobazar_login.enter_phonenumber(userid)
    time.sleep(1)
    hamrobazar_login.enter_password(userpassword)
    time.sleep(1)
    hamrobazar_login.click_login()
    time.sleep(3)
#IMPORT ALL THE NECESSARY MODULES
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import time

from pages.login_page import LoginPage

@pytest.fixture()
def driver():
    #SETTING UP THE CHROME DRIVER MANAGER AS driver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(2)
    #YIELD THE DRIVER
    yield driver
    #CLOSE THE DRIVER INSTANCE
    driver.quit()

def test_login(driver):
    login = LoginPage(driver)
    login.open_page('https://www.olizstore.com/customer/account/login/')
    driver.maximize_window()
    time.sleep(2)
    login.enter_userid("saroj@gmail.com")
    time.sleep(1)
    login.enter_userpassword("Tumblr@123")
    time.sleep(1)
    login.click_login()
    time.sleep(3)



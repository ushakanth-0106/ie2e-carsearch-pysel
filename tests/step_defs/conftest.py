import pytest
from pytest_bdd import given
from selenium import webdriver
from tests.pages.landingpage import LandingPage

APP_URL = 'https://www.webuyanycar.com/'

@pytest.fixture(scope="package", autouse=True)
def my_browser():
    driver = webdriver.Chrome()
    driver.implicitly_wait(30)
    # driver.find_elements('')[1].find_element('')
    driver.maximize_window()
    yield driver
    driver.quit()

@given("User launch the webuyanycar application")
def launch_application(my_browser):
    my_browser.get(APP_URL)
    my_browser.implicitly_wait(30)
    LandingPage(my_browser).click_on_accept_cookies()

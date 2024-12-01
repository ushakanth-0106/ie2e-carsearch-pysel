from selenium.webdriver.common.by import By
# from tests.step_defs.conftest import *

class LandingPage():
    
    def __init__(self, driver):
        self.driver = driver
        self.accept_cookies = (By.CSS_SELECTOR, 'button#onetrust-accept-btn-handler')
        self.input_regnum = (By.ID, 'vehicleReg')
        self.input_mileage = (By.ID, 'Mileage')
        self.btn_submit = (By.ID, 'btn-go')
        self.header_no_details = (By.CSS_SELECTOR, '.page-header h1')


    def click_on_accept_cookies(self):
        self.driver.find_element(*self.accept_cookies).click()
        self.driver.implicitly_wait(30)

    def enter_reg_num(self, vehicleRegNum):
        self.driver.find_element(*self.input_regnum).send_keys(vehicleRegNum)

    def clear_reg_num(self):
        self.driver.find_element(*self.input_regnum).clear()

    def enter_mileage(self, mileageValue):
        self.driver.find_element(*self.input_mileage).send_keys(mileageValue)

    def click_on_btn_submit(self):
        self.driver.find_element(*self.btn_submit).click()
        self.driver.implicitly_wait(60)

    def verify_header_no_details(self):
        sorry_text = self.driver.find_element(*self.header_no_details).text
        if sorry_text == "Sorry, we couldn't find your car":
           print(sorry_text)
           return True
        else:
            return False
        
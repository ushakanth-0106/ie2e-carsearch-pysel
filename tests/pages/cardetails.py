# .d-lg-block.vehicle-details .d-table .d-table-row .heading
from selenium.webdriver.common.by import By

class CarDetails():

    def __init__(self, driver):
        self.driver = driver
        self.car_details = (By.CSS_SELECTOR, '.d-lg-block.vehicle-details')
        self.text_regnum = (By.CLASS_NAME, 'details-vrm')
        self.text_heading = (By.CSS_SELECTOR, '.d-table .d-table-row .heading')
        self.text_value = (By.CSS_SELECTOR, '.d-table .d-table-row .value')
        self.btn_back = (By.ID, 'btn-back')
        self.section_cardetais = (self.driver.find_elements(*self.car_details))[1]

    def verify_car_details_exists(self):
        assert self.section_cardetais.is_displayed(), True

    def click_on_btn_back(self):
        self.driver.find_element(*self.btn_back).click()

    def get_car_num_fromUI(self):
        return self.section_cardetais.find_element(*self.text_regnum).text
    
    def get_additional_car_details(self):
        i = 0
        tmpDet = ""
        for x in self.section_cardetais.find_elements(*self.text_heading):
            if x.text in ("Manufacturer:", "Model:", "Year:"):
                tmpDet = tmpDet + "," + self.section_cardetais.find_elements(*self.text_value)[i].text
            else:
                break
            i += 1
        return tmpDet
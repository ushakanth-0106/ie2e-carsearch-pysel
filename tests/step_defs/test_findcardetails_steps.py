from pytest_bdd import scenarios, given, when, then, parsers
from tests.lib.util import *
from tests.step_defs.conftest import APP_URL
from tests.pages.landingpage import LandingPage
from tests.pages.cardetails import CarDetails

reg_nums = []
cardetails_fromUI = []

scenarios('findcardetails.feature')

@given(parsers.parse("Get the car registration from input file \'{ip_file}\'"))
def read_input_file(ip_file):
    ip_lines = read_file(ip_file)
    global reg_nums
    regplate = get_reg_number(ip_lines)
    reg_nums = [rp.replace(" ", "") for rp in regplate]
    print(reg_nums)


@when('User retrieves car details from UI based on reg')
def retrieve_car_details(my_browser):
    global cardetails_fromUI
    for x in reg_nums:        
        LandingPage(my_browser).enter_reg_num(x)
        LandingPage(my_browser).enter_mileage('45000')
        LandingPage(my_browser).click_on_btn_submit()
        if LandingPage(my_browser).verify_header_no_details() == False:
            CarDetails(my_browser).verify_car_details_exists()
            tempDetails = ""
            tempDetails = CarDetails(my_browser).get_car_num_fromUI()
            assert tempDetails, x
            cardetails_fromUI.append(tempDetails + CarDetails(my_browser).get_additional_car_details())
            print(cardetails_fromUI)
            CarDetails(my_browser).click_on_btn_back()
        else:
            LandingPage(my_browser).clear_reg_num()
        
        my_browser.get(APP_URL)
        my_browser.implicitly_wait(30)


@then(parsers.parse("I compare with output file data \'{op_file}\'"))
def compare_output_file(op_file):
    write_file(op_file, cardetails_fromUI)


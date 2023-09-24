import time

import pytest
from selenium import webdriver
#from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By


@pytest.fixture()
def driver():
    print("Opening Chrome driver")
    provided_driver = webdriver.Chrome()
    provided_driver.implicitly_wait(5)
    yield provided_driver
    print("\n Closing Chrome driver")
    provided_driver.quit()


class CourseAttendancePayment:
    # Class variables (shared among all instances)
    class_variable = 0

    # Constructor method (called when an object is created)
    def __init__(self, name, position, city, amount):
        # Instance variables (unique to each instance)
        self.name = name
        self.position = position
        self.city = city
        self.amount = amount


class TestNavigateTableScenarios:
    @pytest.mark.challenge
    def test_navigate_table(self,driver):
        time.sleep(1)

        driver.get("https://rahulshettyacademy.com/AutomationPractice/")
        found_table = driver.find_element(By.CSS_SELECTOR,'.tableFixHead #product')
        rows_table_list = found_table.find_elements(By.TAG_NAME,"tr")
        rows_count = len(rows_table_list)
        print("we found {} rows".format(rows_count))
        course_attendance_payments = []
        types_of_role_found = set()
        time.sleep(2)
        iterator_on_rows = iter(rows_table_list)
        next(iterator_on_rows)

        for row in iterator_on_rows:
            cells_in_row = row.find_elements(By.TAG_NAME,"td")
            name = cells_in_row[0].text
            position = cells_in_row[1].text
            city = cells_in_row[2].text
            amount = cells_in_row[3].text
            #print("We found a row name {}, position {}, city {}, amount {} ".format(name, position, city, amount))
            found_course_attendance_payment = CourseAttendancePayment(name, position, city, amount)
            course_attendance_payments.append(found_course_attendance_payment)
            types_of_role_found.add(position)

    # we can now do some list comprehensions
        attendees_from_chennai = [attendee for attendee in course_attendance_payments if attendee.city == 'Chennai']
        assert len(attendees_from_chennai) == 4, 'Incorrect number of Chennai Attendees - should be 4'

        expected_Roles=('Engineer','Mechanic','Manager','Receptionist','Businessman','Postman','Sportsman','Cricketer')
        unexpected_Roles = types_of_role_found.difference(expected_Roles)
        assert len(unexpected_Roles) == 0, "Unexpected roles found - {}".format(unexpected_Roles)
    #assert log_out_btn_locator.is_displayed()
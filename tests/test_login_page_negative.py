import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture()
def driver():
    print("Opening Chrome driver")
    provided_driver = webdriver.Chrome()
    yield provided_driver
    print("\n Closing Chrome driver")
    provided_driver.quit()


class TestNegativeScenarios:
    @pytest.mark.login
    @pytest.mark.negative
    def test_negative_username(self, driver):
        # startbrowser
        # driver = webdriver.Chrome()
        time.sleep(1)

        # Open page
        driver.get("https://practicetestautomation.com/practice-test-login/")

        time.sleep(2)

        # Define our locators together
        username_locator = driver.find_element(By.ID, "username")
        password_locator = driver.find_element(By.NAME, "password")
        submit_locator = driver.find_element(By.XPATH, "//button[@class='btn']")

        # Type incorrect username into Username field
        # Type password Password123 into Password field
        username_locator.send_keys("incorrectUser")
        password_locator.send_keys("Password123")
        # Push Submit button
        submit_locator.click()
        time.sleep(2)

        # Verify error message is displayed
        error_text_locator = driver.find_element(By.XPATH, "//div[@id='error']")
        assert error_text_locator.is_displayed(), "The Error text should have been displayed"

        # Verify error message text is Your username is invalid!
        assert error_text_locator.text == "Your username is invalid!", \
            "The error text does not have the right textual contents - username error"

    @pytest.mark.login
    @pytest.mark.negative
    def test_negative_password(self, driver):
        # startbrowser
        # driver = webdriver.Chrome()
        time.sleep(1)

        # Open page
        driver.get("https://practicetestautomation.com/practice-test-login/")

        time.sleep(2)

        username_locator = driver.find_element(By.ID, "username")
        password_locator = driver.find_element(By.NAME, "password")

        # Push Submit button
        submit_locator = driver.find_element(By.XPATH, "//button[@class='btn']")

        # Type username student into Username field
        # Type incorrect password into Password field
        username_locator.send_keys("student")
        password_locator.send_keys("incorrectPassword123")

        # Push Submit button
        submit_locator.click()
        time.sleep(2)

        # Verify error message is displayed
        error_text_locator = driver.find_element(By.XPATH, "//div[@id='error']")
        assert error_text_locator.is_displayed(), "The Error text should have been displayed"

        # Verify error message text is Your username is invalid!
        assert error_text_locator.text == "Your password is invalid!", \
            "The error text does not have the right textual contents - password error"

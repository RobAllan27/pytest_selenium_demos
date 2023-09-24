import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestPositiveScenarios:
    @pytest.mark.login
    @pytest.mark.positive
    def test_positive_login(self):

        # startbrowser
        driver = webdriver.Chrome()
        time.sleep(1)

        # Open page
        driver.get("https://practicetestautomation.com/practice-test-login/")

        time.sleep(2)

        # Type username student into Username field
        username_locator = driver.find_element(By.ID, "username")

        # Type password Password123 into Password field
        password_locator = driver.find_element(By.NAME, "password")

        # Push Submit button
        submit_locator = driver.find_element(By.XPATH, "//button[@class='btn']")

        username_locator.send_keys("student")
        password_locator.send_keys("Password123")
        submit_locator.click()
        time.sleep(2)

        # Verify new page URL contains practicetestautomation.com/logged-in-successfully/
        actual_current_url = driver.current_url

        assert actual_current_url == "https://practicetestautomation.com/logged-in-successfully/"

        # assert actual_current_url == "practicetestautomation.com/logged-in-successfully"

        # Verify new page contains expected text ('Congratulations' or 'successfully logged in')
        logged_in_text_locator = driver.find_element(By.TAG_NAME, "h1")
        actual_logged_in_text = logged_in_text_locator.text
        assert actual_logged_in_text == "Logged In Successfully"

        # Verify button Log out is displayed on the new page
        log_out_btn_locator = driver.find_element(By.LINK_TEXT, "Log out")
        assert log_out_btn_locator.is_displayed()

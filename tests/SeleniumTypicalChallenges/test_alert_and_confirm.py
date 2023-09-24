import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture()
def driver():
    print("Opening Chrome driver")
    provided_driver = webdriver.Chrome()
    provided_driver.implicitly_wait(5)
    yield provided_driver
    print("\n Closing Chrome driver")
    provided_driver.quit()


class TestAlertScenarios:
    @pytest.mark.challenge
    def test_navigate_alert_window(self, driver):
        time.sleep(1)

        driver.get("https://rahulshettyacademy.com/AutomationPractice/")
        name_field_element = driver.find_element(By.CSS_SELECTOR, "input.inputs[name='enter-name'")
        chosen_name_for_alert = "Rob"
        name_field_element.send_keys(chosen_name_for_alert)
        alert_key_element = driver.find_element(By.XPATH, "//input[@id='alertbtn']")
        alert_key_element.click()
        alert = driver.switch_to.alert
        found_alert_text = alert.text
        alert.accept()
        expected_text = "Hello {}, share this practice page and share your knowledge"
        expected_text_for_alert = expected_text.format(chosen_name_for_alert)

        assert found_alert_text == expected_text_for_alert, \
            "We got the wrong alert text - we got {} as text".format(found_alert_text)

    @pytest.mark.challenge
    def test_navigate_confirm_window_with_dismiss(self, driver):
        time.sleep(1)

        # TODO to consolidate this and next test to single method

        driver.get("https://rahulshettyacademy.com/AutomationPractice/")
        name_field_element = driver.find_element(By.CSS_SELECTOR, "input.inputs[name='enter-name'")
        chosen_name_for_alert = "Rob"
        name_field_element.send_keys(chosen_name_for_alert)
        confirm_key_element = driver.find_element(By.XPATH, "//input[@id='confirmbtn']")
        confirm_key_element.click()
        alert = driver.switch_to.alert
        found_alert_text = alert.text
        alert.dismiss()
        expected_text = "Hello {}, Are you sure you want to confirm?"
        expected_text_for_alert = expected_text.format(chosen_name_for_alert)

        assert found_alert_text == expected_text_for_alert, \
            "We got the wrong alert text - we got {} as text".format(found_alert_text)

    @pytest.mark.challenge
    def test_navigate_confirm_window_with_accept(self, driver):
        time.sleep(1)

        # TODO to consolidate this and previous to single method

        driver.get("https://rahulshettyacademy.com/AutomationPractice/")
        name_field_element = driver.find_element(By.CSS_SELECTOR, "input.inputs[name='enter-name'")
        chosen_name_for_alert = "Rob"
        name_field_element.send_keys(chosen_name_for_alert)
        confirm_key_element = driver.find_element(By.XPATH, "//input[@id='confirmbtn']")
        confirm_key_element.click()
        alert = driver.switch_to.alert
        found_alert_text = alert.text
        alert.accept()
        expected_text = "Hello {}, Are you sure you want to confirm?"
        expected_text_for_alert = expected_text.format(chosen_name_for_alert)

        assert found_alert_text == expected_text_for_alert, \
            "We got the wrong alert text - we got {} as text".format(found_alert_text)

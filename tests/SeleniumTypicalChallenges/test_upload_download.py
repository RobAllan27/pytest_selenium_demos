import time

import pytest
from selenium import webdriver
#from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains


@pytest.fixture()
def driver():
    print("Opening Chrome driver")
    provided_driver = webdriver.Chrome()
    provided_driver.implicitly_wait(5)
    yield provided_driver
    print("\n Closing Chrome driver")
    provided_driver.quit()


class TestFileScenarios:


    @pytest.mark.challenge
    def test_download_file(self,driver):
        time.sleep(1)
        driver.get("https://www.softwaretestingmaterial.com/sample-webpage-to-automate/")
        dropdown = driver.find_element(By.XPATH,"// a[@ href='https://drive.google.com/uc?export=download&id=0B5QPGtxBy7lgQTZ6bTVZQUhwTXc']")


        '''
        Actions tested here but not terribly effective
        actions = ActionChains(driver)
        actions.move_to_element(dropdown).perform()
        '''

        options = webdriver.ChromeOptions();
        prefs = {"download.default_directory" : "C:\\user\\robma\\Downloads"}
        options.add_experimental_option("prefs", prefs)

        driver.execute_script("arguments[0].scrollIntoView(true);", dropdown)

        dropdown.click()

        time.sleep(2)

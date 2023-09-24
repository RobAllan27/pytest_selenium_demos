import time

import pytest
from selenium import webdriver
#from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@pytest.fixture()
def driver():
    print("Opening Chrome driver")
    provided_driver = webdriver.Chrome()
    provided_driver.implicitly_wait(5)
    yield provided_driver
    print("\n Closing Chrome driver")
    provided_driver.quit()


class TestNavigationScenarios:
    @pytest.mark.challenge
    def test_navigate_radio_buttons(self, driver):
        time.sleep(1)

        driver.get("https://rahulshettyacademy.com/AutomationPractice/")
        radio_button_list = driver.find_elements(By.CSS_SELECTOR, "fieldset [for^='radio'] input")
        radio_button_count = len(radio_button_list)
        print("We found {} radio buttons".format(radio_button_count))
        iterator_on_radio_button = iter(radio_button_list)

        assert radio_button_count == 3, \
            "We should have 3 radio buttons - but only found {} buttons".format(radio_button_count)

        for radio_button in iterator_on_radio_button:
            radio_button.click()
            time.sleep(1)
            name_of_selected_radio_button = radio_button.text
            assert radio_button.is_selected(), \
                "Rado Button should be selected - {}".format(name_of_selected_radio_button)

    @pytest.mark.challenge
    def test_navigate_checkbox_suggestion(self, driver):
        time.sleep(1)

        driver.get("https://rahulshettyacademy.com/AutomationPractice/")
        check_button_list = driver.find_elements(By.CSS_SELECTOR, "#checkbox-example input[name^='checkBoxOption']")
        check_button_list_count = len(check_button_list)
        print("We found {} radio buttons".format(check_button_list_count))
        iterator_on_check_button = iter(check_button_list)

        assert check_button_list_count == 3, \
            "We should have 3 radio buttons - but only found {} buttons".format(check_button_list_count)
        number_of_times_we_selected_check_boxes = 0

        for check_button in iterator_on_check_button:
            check_button.click()
            number_of_times_we_selected_check_boxes = number_of_times_we_selected_check_boxes + 1
            currently_selected_check_boxes = [check_button for check_button in check_button_list if check_button.is_selected()]
            assert len(currently_selected_check_boxes) == number_of_times_we_selected_check_boxes, ("Number of "
                                                                                                    "selected "
                                                                                                    "checkboxes - {} "
                                                                                                    "- but should be "
                                                                                                    "").format(len(
                currently_selected_check_boxes), number_of_times_we_selected_check_boxes)
            time.sleep(5)

    @pytest.mark.challenge
    def test_navigate_suggestion_list(self, driver):
        time.sleep(1)

        driver.get("https://rahulshettyacademy.com/AutomationPractice/")
        suggestion_list_input = driver.find_element(By.CSS_SELECTOR, \
                                                    "#autocomplete[placeholder='Type to Select Countries']")
        suggestion_list_input.send_keys("Aust")
        time.sleep(2)
        list_of_suggested_countries_elements = driver.find_elements(By.CSS_SELECTOR, \
                                                                    ".ui-autocomplete .ui-menu-item-wrapper")
        iterator_on_suggested_countries = iter(list_of_suggested_countries_elements)
        suggested_country_names_set = set()

        for suggested_country_element in iterator_on_suggested_countries:
            suggested_country_names_set.add(suggested_country_element.text)

        print("Country set {}".format(
                suggested_country_names_set))
        expected_set_of_countries = {'Australia', 'Austria'}

        missing_countries_from_suggestions = expected_set_of_countries.difference(suggested_country_names_set)

        assert len(missing_countries_from_suggestions) == 0, "We should have got the right suggestions - but got different suggestions".format(
                missing_countries_from_suggestions)

    @pytest.mark.challenge
    def test_navigate_drop_down_single_selection(self, driver):
        time.sleep(1)
        driver.get("https://rahulshettyacademy.com/AutomationPractice/")
        dropdown = driver.find_element(By.CSS_SELECTOR, "#dropdown-class-example")
        dropdown.click()
        select = Select(dropdown)
        select.select_by_index(0)
        time.sleep(2)
        select.select_by_index(1)
        time.sleep(2)
        select.select_by_index(2)
        time.sleep(2)

        select.select_by_value('option3')
        assert select.first_selected_option.text == 'Option3', "We should at this stage have option 3 selected"

    @pytest.mark.challenge
    def test_navigate_drop_down_multiple_selection(self, driver):
        time.sleep(1)
        driver.get("https://www.softwaretestingmaterial.com/sample-webpage-to-automate/")
        dropdown = driver.find_element(By.CSS_SELECTOR, ".spTextField[name='multipleselect[]']")

        '''
        Actions tested here but not terribly effective
        actions = ActionChains(driver)
        actions.move_to_element(dropdown).perform()
        '''

        driver.execute_script("arguments[0].scrollIntoView(true);", dropdown)

        dropdown.click()
        select = Select(dropdown)
        select.select_by_index(0)
        time.sleep(2)
        select.select_by_value('msmanual')
        time.sleep(2)
        select.select_by_index(2)
        time.sleep(2)
        currently_selected_options = select.all_selected_options

        iterator_on_currently_selected_options = iter(currently_selected_options)
        text_for_selected_options = set()

        for web_element_in_selected_countries in iterator_on_currently_selected_options:
            text_for_selected_options.add(web_element_in_selected_countries.text)

        expected_set_of_selected_options = {'Performance Testing', 'Manual Testing', 'Agile Methodology'}

        missing_selections = expected_set_of_selected_options.difference(text_for_selected_options)

        assert len(missing_selections) == 0, "We should have got the right selections - but we have some missing selections {}".format(
            missing_selections)

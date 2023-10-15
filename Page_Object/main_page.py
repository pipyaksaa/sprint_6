import pytest

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import DropdownLocators


class MainPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open(self):
        self.driver.get("https://qa-scooter.praktikum-services.ru/")

    def click_dropdown_button(self, button_number):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(
            DropdownLocators.BUTTON_CONFIRM))
        self.driver.find_element(*DropdownLocators.BUTTON_CONFIRM).click()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        dropdown_element_locator = getattr(DropdownLocators, f'DROPDOWN_ELEMENT_{button_number}', None)

        if dropdown_element_locator:
            self.driver.find_element(*dropdown_element_locator).click()
        else:
            raise ValueError(f"Invalid button_number: {button_number}")


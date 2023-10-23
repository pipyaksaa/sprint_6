from allure_commons._allure import step
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver: webdriver):
        self.driver = driver

    @step("Open the page")
    def open_page(self, url):
        self.driver.get(url)

    @step("Wait for element to be visible")
    def wait_for_element_to_be_visible(self, locator):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(locator)
        )

    @step("Find element")
    def find_element(self, locator):
        self.driver.find_element(*locator)

    @step("Click element")
    def click_element(self, locator):
        self.driver.find_element(*locator).click()

    @step("Scroll to the bottom of the page")
    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    @step("Wait for element to be clickable")
    def wait_for_element_to_be_clickable(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            expected_conditions.element_to_be_clickable(locator)
        )

    @step("Wait for element to be present")
    def wait_for_element_to_be_present(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            expected_conditions.presence_of_element_located(locator)
        )

    @step("Wait for element to be visible for expected condition")
    def wait_for_element_to_be_visible_expected_condition(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            expected_conditions.visibility_of_element_located(locator)
        )

    @step("Send keys in form")
    def enter_text(self, locator, text):
        element = self.driver.find_element(*locator)
        element.send_keys(text)

    @step("Open new tab")
    def switch_to_new_window(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])
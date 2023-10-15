from selenium.webdriver.common import actions
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import OrderLocators, DropdownLocators
from selenium.webdriver.common.by import By

class OrderScooter:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://qa-scooter.praktikum-services.ru/")

    def open_order_page(self, ORDER_BUTTON_UPPER):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(
            DropdownLocators.BUTTON_CONFIRM))
        self.driver.find_element(*DropdownLocators.BUTTON_CONFIRM).click()
        self.driver.find_element(*ORDER_BUTTON_UPPER).click()

    def fill_order_form(self, name, last_name, address, phone):
        WebDriverWait(self.driver, 6).until(expected_conditions.element_to_be_clickable(OrderLocators.NEXT_BUTTON))
        self.driver.find_element(*OrderLocators.NAME_INPUT).send_keys(name)
        self.driver.find_element(*OrderLocators.LAST_NAME_INPUT).send_keys(last_name)
        self.driver.find_element(*OrderLocators.ADDRESS_INPUT).send_keys(address)
        self.driver.find_element(*OrderLocators.METRO_INPUT).click()
        WebDriverWait(self.driver, 6).until(expected_conditions.element_to_be_clickable(OrderLocators.CHEKBOX_LOKATOR))
        self.driver.find_element(*OrderLocators.CHEKBOX_LOKATOR).click()
        self.driver.find_element(*OrderLocators.PHONE_INPUT).send_keys(phone)
        self.driver.find_element(*OrderLocators.NEXT_BUTTON).click()

    def fill_form_about_rent(self, date, comment):
        self.driver.find_element(*OrderLocators.DELIVERY_DATE_INPUT).send_keys(date)
        self.driver.find_element(*OrderLocators.TEXT).click()
        self.driver.find_element(*OrderLocators.DROPDOWN_ELEMENT).click()
        self.driver.find_element(*OrderLocators.DROPDOWN_MENU_DAY).click()
        self.driver.find_element(*OrderLocators.CHECKBOXES_ELEMENT).click()
        self.driver.find_element(*OrderLocators.COURIER_COMMENT_INPUT).send_keys(comment)
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(OrderLocators.ORDER_BUTTON_ACCEPT)).click()
        self.driver.find_element(*OrderLocators.ORDER_BUTTON_ACCEPT).click()

    def get_success_message(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(OrderLocators.YES_BUTTON))
        self.driver.find_element(*OrderLocators.YES_BUTTON).click()
        self.driver.find_element(*OrderLocators.VIEW_STATUS_BUTTON).click()
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "div.Order_Modal__YZ-d3")))

    def go_to_home_page(self):
        self.driver.find_element(*OrderLocators.SCOOTER_IMAGE).click()

    def go_to_yandex_home_page(self):
        self.driver.find_element(*OrderLocators.YANDEX_IMAGE).click()

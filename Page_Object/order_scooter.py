import allure
from selenium.webdriver.common import actions
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Page_Object.base_page import BasePage
from locators import OrderLocators, DropdownLocators
from selenium.webdriver.common.by import By

class OrderScooter(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.page_url = "https://qa-scooter.praktikum-services.ru/"

    @allure.step("Open the main page")
    def open(self):
        super().open_page(self.page_url)

    @allure.step("Open order page")
    def open_order_page(self, ORDER_BUTTON_UPPER):
        self.wait_for_element_to_be_visible(DropdownLocators.BUTTON_CONFIRM)
        self.click_element(DropdownLocators.BUTTON_CONFIRM)
        self.driver.find_element(*ORDER_BUTTON_UPPER).click()

    @allure.step("Fill order form")
    def fill_order_form(self, name, last_name, address, phone):
        self.wait_for_element_to_be_clickable(OrderLocators.NEXT_BUTTON)
        self.driver.find_element(*OrderLocators.NAME_INPUT).send_keys(name)
        self.driver.find_element(*OrderLocators.LAST_NAME_INPUT).send_keys(last_name)
        self.driver.find_element(*OrderLocators.ADDRESS_INPUT).send_keys(address)
        self.driver.find_element(*OrderLocators.METRO_INPUT).click()
        self.wait_for_element_to_be_clickable(OrderLocators.CHEKBOX_LOKATOR)
        self.driver.find_element(*OrderLocators.CHEKBOX_LOKATOR).click()
        self.driver.find_element(*OrderLocators.PHONE_INPUT).send_keys(phone)
        self.driver.find_element(*OrderLocators.NEXT_BUTTON).click()

    @allure.step("Fill order form about rent")
    def fill_form_about_rent(self, date, comment):
        self.driver.find_element(*OrderLocators.DELIVERY_DATE_INPUT).send_keys(date)
        self.driver.find_element(*OrderLocators.TEXT).click()
        self.driver.find_element(*OrderLocators.DROPDOWN_ELEMENT).click()
        self.driver.find_element(*OrderLocators.DROPDOWN_MENU_DAY).click()
        self.driver.find_element(*OrderLocators.CHECKBOXES_ELEMENT).click()
        self.driver.find_element(*OrderLocators.COURIER_COMMENT_INPUT).send_keys(comment)
        self.wait_for_element_to_be_clickable(OrderLocators.ORDER_BUTTON_ACCEPT)
        self.driver.find_element(*OrderLocators.ORDER_BUTTON_ACCEPT).click()

    @allure.step("Check order massage")
    def get_success_message(self):
        self.wait_for_element_to_be_clickable(OrderLocators.YES_BUTTON)
        self.driver.find_element(*OrderLocators.YES_BUTTON).click()

    @allure.step("Check scooter image")
    def go_to_home_page(self):
        self.driver.find_element(*OrderLocators.SCOOTER_IMAGE).click()

    @allure.step("Check yandex image")
    def go_to_yandex_home_page(self):
        self.wait_for_element_to_be_visible(DropdownLocators.BUTTON_CONFIRM)
        self.click_element(DropdownLocators.BUTTON_CONFIRM)
        self.driver.find_element(*OrderLocators.YANDEX_IMAGE).click()

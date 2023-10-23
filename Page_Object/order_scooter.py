import allure
from Page_Object.base_page import BasePage
from locators import OrderLocators, DropdownLocators
from data import test_user

class OrderScooter(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.page_url = "https://qa-scooter.praktikum-services.ru/"

    @allure.step("Open the main page")
    def open(self):
        super().open_page(self.page_url)

    @allure.step("Open order page")
    def open_order_page(self, button_locator):
        self.wait_for_element_to_be_visible(DropdownLocators.BUTTON_CONFIRM)
        self.click_element(DropdownLocators.BUTTON_CONFIRM)
        self.click_element(button_locator)


    @allure.step("Fill order form")
    def fill_order_form(self, name, last_name, address, phone):
        self.wait_for_element_to_be_clickable(OrderLocators.NEXT_BUTTON)
        self.enter_text(OrderLocators.NAME_INPUT, name)
        self.enter_text(OrderLocators.LAST_NAME_INPUT, last_name)
        self.enter_text(OrderLocators.ADDRESS_INPUT, address)
        self.click_element(OrderLocators.METRO_INPUT)
        self.wait_for_element_to_be_clickable(OrderLocators.CHEKBOX_LOKATOR)
        self.click_element(OrderLocators.CHEKBOX_LOKATOR)
        self.enter_text(OrderLocators.PHONE_INPUT, phone)
        self.click_element(OrderLocators.NEXT_BUTTON)

    @allure.step("Fill order form about rent")
    def fill_form_about_rent(self, date, comment):
        self.enter_text(OrderLocators.DELIVERY_DATE_INPUT, date)
        self.click_element(OrderLocators.TEXT)
        self.click_element(OrderLocators.DROPDOWN_ELEMENT)
        self.click_element(OrderLocators.DROPDOWN_MENU_DAY)
        self.click_element(OrderLocators.CHECKBOXES_ELEMENT)
        self.enter_text(OrderLocators.COURIER_COMMENT_INPUT, comment)
        self.wait_for_element_to_be_clickable(OrderLocators.ORDER_BUTTON_ACCEPT)
        self.click_element(OrderLocators.ORDER_BUTTON_ACCEPT)

    @allure.step("Check order massage")
    def get_success_message(self):
        self.wait_for_element_to_be_clickable(OrderLocators.YES_BUTTON)
        self.find_element(OrderLocators.YES_BUTTON)

    @allure.step("Check scooter image")
    def go_to_home_page(self):
        self.click_element(OrderLocators.SCOOTER_IMAGE)

    @allure.step("Check yandex image")
    def go_to_yandex_home_page(self):
        self.wait_for_element_to_be_visible(DropdownLocators.BUTTON_CONFIRM)
        self.click_element(DropdownLocators.BUTTON_CONFIRM)
        self.click_element(OrderLocators.YANDEX_IMAGE)
        self.switch_to_new_window()
        self.wait_for_element_to_be_visible(OrderLocators.DZEN)

import allure
from locators import DropdownLocators
from Page_Object.base_page import BasePage

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.page_url = "https://qa-scooter.praktikum-services.ru/"

    @allure.step("Open the main page")
    def open(self):
        super().open_page(self.page_url)

    @allure.step("Open dropdown")
    def click_dropdown_button(self, button_number):
        self.wait_for_element_to_be_visible(DropdownLocators.BUTTON_CONFIRM)
        self.click_element(DropdownLocators.BUTTON_CONFIRM)
        self.scroll_to_bottom()
        dropdown_element_locator = getattr(DropdownLocators, f'DROPDOWN_ELEMENT_{button_number}', None)
        if dropdown_element_locator:
            self.click_element(dropdown_element_locator)

    @allure.step("Check dropdown text")
    def get_dropdown_text(self, button_number):
        return self.driver.find_element(*getattr(DropdownLocators, f'DROPDOWN_TEXT_{button_number}')).text

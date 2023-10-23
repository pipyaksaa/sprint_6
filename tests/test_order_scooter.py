import allure
import pytest
from conftest import driver
from Page_Object.order_scooter import OrderScooter
from locators import OrderLocators
from data import test_user


class TestScooterOrder:
    @pytest.mark.parametrize("button_locator", [OrderLocators.ORDER_BUTTON_UPPER, OrderLocators.ORDER_BUTTON_DOWN])
    @allure.title("Тест заказа скутера")
    @allure.description("Проверка заказа скутера на веб-сайте")
    def test_order_scooter(self, driver, button_locator):
        order_scooter = OrderScooter(driver)
        order_scooter.open()
        order_scooter.open_order_page(button_locator)
        test_user_data = test_user
        name = test_user_data["name"]
        last_name = test_user_data["last_name"]
        address = test_user_data["address"]
        phone = test_user_data["phone"]
        date = test_user_data["date"]
        comment = test_user_data["comment"]
        order_scooter.fill_order_form(name, last_name, address, phone)
        order_scooter.fill_form_about_rent(date, comment)
        order_scooter.get_success_message()
        assert driver.find_element(*OrderLocators.VIEW_STATUS_FORM) is not None

class TestClickScooterLogo:
    @allure.title("Тест открытия главной страницы")
    @allure.description("Проверка что открылась главная страница")
    def test_go_to_home_page(self, driver):
        order_scooter = OrderScooter(driver)
        order_scooter.open()
        order_scooter.open_order_page(OrderLocators.ORDER_BUTTON_UPPER)
        order_scooter.go_to_home_page()
        current_url = driver.current_url
        expected_url = "https://qa-scooter.praktikum-services.ru/"
        assert current_url == expected_url, f"Expected URL: {expected_url}, Actual URL: {current_url}"

class TestClickYandexLogo:
    @allure.title("Тест открытия Дзен страницы")
    @allure.description("роверка что открылась Дзен страница в новой вкладке")
    def test_go_to_yandex_home_page(self, driver):
        order_scooter = OrderScooter(driver)
        order_scooter.open()
        order_scooter.go_to_yandex_home_page()
        expected_url = "https://dzen.ru/?yredirect=true"
        assert driver.current_url == expected_url

import allure
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from conftest import driver
from Page_Object.order_scooter import OrderScooter
from locators import OrderLocators
from data import test_user

@allure.title("Тест заказа скутера")
@allure.description("Проверка заказа скутера на веб-сайте")
@pytest.mark.parametrize("button_locator", [OrderLocators.ORDER_BUTTON_UPPER, OrderLocators.ORDER_BUTTON_DOWN])
def test_order_scooter(driver, button_locator):
    order_scooter = OrderScooter(driver)
    order_scooter.open()
    order_scooter.open_order_page(button_locator)

    name = test_user["name"]
    last_name = test_user["last_name"]
    address = test_user["address"]
    phone = test_user["phone"]
    date = test_user["date"]
    comment = test_user["comment"]

    order_scooter.fill_order_form(name, last_name, address, phone)
    order_scooter.fill_form_about_rent(date, comment)
    order_scooter.get_success_message()
    assert driver.find_element(*OrderLocators.VIEW_STATUS_FORM) is not None

def test_go_to_home_page(driver):
    order_scooter = OrderScooter(driver)
    order_scooter.open()
    order_scooter.open_order_page(OrderLocators.ORDER_BUTTON_UPPER)
    order_scooter.go_to_home_page()
    current_url = driver.current_url
    expected_url = "https://qa-scooter.praktikum-services.ru/"
    assert current_url == expected_url, f"Expected URL: {expected_url}, Actual URL: {current_url}"

def test_go_to_yandex_home_page(driver):
    order_scooter = OrderScooter(driver)
    order_scooter.open()
    order_scooter.go_to_yandex_home_page()
    driver.switch_to.window(driver.window_handles[-1])
    expected_url = "https://dzen.ru/?yredirect=true"
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(OrderLocators.DZEN))
    assert driver.current_url == expected_url
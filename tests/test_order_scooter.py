import allure
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from conftest import driver
from Page_Object.order_scooter import OrderScooter
from locators import OrderLocators

@allure.title("Тест заказа скутера")
@allure.description("Проверка заказа скутера на веб-сайте")
@pytest.mark.parametrize("button_locator", [OrderLocators.ORDER_BUTTON_UPPER, OrderLocators.ORDER_BUTTON_DOWN])
def test_order_scooter(driver, button_locator):
    order_scooter = OrderScooter(driver)
    order_scooter.open()
    order_scooter.open_order_page(button_locator)

    name = "Регина"
    last_name = "Ходаковская"
    address = "Ваш адрес введите полностью"
    phone = "998977606789"
    date = "17.10.2023"
    comment = "Ваш комментарий"

    order_scooter.fill_order_form(name, last_name, address, phone)

    order_scooter.fill_form_about_rent(date, comment)

    order_scooter.get_success_message()
    from selenium.webdriver.support import expected_conditions
    assert WebDriverWait(driver, 2).until(expected_conditions.element_to_be_clickable(
        (By.CSS_SELECTOR, "div.Order_ModalHeader__3FDaJ')]"))) is not None

    order_scooter.go_to_home_page()
    current_url = driver.current_url
    expected_url = "https://qa-scooter.praktikum-services.ru/"
    assert current_url == expected_url, f"Expected URL: {expected_url}, Actual URL: {current_url}"

    order_scooter.go_to_yandex_home_page()
    driver.switch_to.window(driver.window_handles[-1])
    assert "https://www.yandex.ru" in driver.current_url



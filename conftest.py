import pytest
from selenium import webdriver
from Page_Object.order_scooter import OrderScooter

@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()

@pytest.fixture(scope='function')
def order_scooter(driver):
    order_page = OrderScooter(driver)
    order_page.open()
    return order_page

import pytest
import allure
from conftest import driver
from Page_Object.main_page import MainPage


class TestDropdown:
    @pytest.mark.parametrize("button_number, expected_text", [
        (1, "Сутки — 400 рублей. Оплата курьеру — наличными или картой."),
        (2, "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."),
        (3, "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."),
        (4, "Только начиная с завтрашнего дня. Но скоро станем расторопнее."),
        (5, "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."),
        (6, "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."),
        (7, "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."),
        (8, "Да, обязательно. Всем самокатов! И Москве, и Московской области.")
    ])
    @allure.title("Test Dropdown Elements")
    @allure.description("Test the text of dropdown elements")
    def test_dropdown_elements(self, driver, button_number, expected_text):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_dropdown_button(button_number)
        dropdown_text = main_page.get_dropdown_text(button_number)
        assert dropdown_text == expected_text, f"Expected text: '{expected_text}', but got: '{dropdown_text}'"
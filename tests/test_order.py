import allure
import pytest

from data import ORDER_DATA
from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestOrder:

    @allure.title("Оформление заказа ({entry_point}, {data[name]} {data[surname]})")
    @pytest.mark.parametrize("entry_point", ["top", "bottom"])
    @pytest.mark.parametrize("data", ORDER_DATA)
    def test_order_full_flow(self, driver, data, entry_point):
        main = MainPage(driver)
        main.accept_cookies()

        if entry_point == "top":
            main.click_order_button_top()
        else:
            main.click_order_button_bottom()

        order = OrderPage(driver)
        order.fill_first_form(data)
        order.fill_second_form(data)
        order.confirm_order()

        assert order.is_order_success()

    @allure.title("Переход на главную через логотип Самоката")
    def test_scooter_logo_redirects_home(self, driver):
        main = MainPage(driver)
        main.accept_cookies()
        main.click_scooter_logo()

        assert driver.current_url == "https://qa-scooter.education-services.ru/"

    @allure.title("Переход на Дзен через логотип Яндекса")
    def test_yandex_logo_redirects_to_dzen(self, driver):
        main = MainPage(driver)
        main.accept_cookies()
        main.click_yandex_logo()
        main.switch_to_new_window()

        main.wait.until(lambda d: "dzen.ru" in d.current_url or "ya.ru" in d.current_url)
        assert "dzen.ru" in driver.current_url or "ya.ru" in driver.current_url
import allure
import pytest

from data import ORDER_DATA
from urls import BASE_URL, YA_URL
from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestOrder:

    @allure.title("Заказ через верхнюю кнопку ({data[name]} {data[surname]})")
    @pytest.mark.parametrize("data", ORDER_DATA)
    def test_order_from_top_button(self, driver, data):
        main = MainPage(driver)
        main.accept_cookies()
        main.click_order_button_top()

        order = OrderPage(driver)
        order.fill_first_form(data)
        order.fill_second_form(data)
        order.confirm_order()

        assert order.is_order_success()

    @allure.title("Заказ через нижнюю кнопку ({data[name]} {data[surname]})")
    @pytest.mark.parametrize("data", ORDER_DATA)
    def test_order_from_bottom_button(self, driver, data):
        main = MainPage(driver)
        main.accept_cookies()
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

        assert main.get_current_url() == BASE_URL

    @allure.title("Переход на Дзен через логотип Яндекса")
    def test_yandex_logo_redirects_to_ya(self, driver):
        main = MainPage(driver)
        main.accept_cookies()
        main.click_yandex_logo()
        main.switch_to_new_window()
        main.wait_for_url_contains(YA_URL)

        assert YA_URL in main.get_current_url()

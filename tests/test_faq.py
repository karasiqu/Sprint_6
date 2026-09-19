import allure
import pytest

from data import FAQ_DATA
from pages.main_page import MainPage


class TestFaq:

    @allure.title("Проверка вопроса FAQ №{num}")
    @pytest.mark.parametrize("num, expected_answer", FAQ_DATA)
    def test_faq_question(self, driver, num, expected_answer):
        page = MainPage(driver)
        page.accept_cookies()
        page.scroll_to_faq(num)
        page.click_faq_question(num)

        assert expected_answer in page.get_faq_answer_text(num)
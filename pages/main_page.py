from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    def scroll_to_faq(self, num):
        locator = (
            MainPageLocators.FAQ_QUESTION[0],
            MainPageLocators.FAQ_QUESTION[1].format(num=num),
        )
        element = self.find(locator)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", element
        )

    def click_faq_question(self, num):
        locator = (
            MainPageLocators.FAQ_QUESTION[0],
            MainPageLocators.FAQ_QUESTION[1].format(num=num),
        )
        self.click(locator)

    def get_faq_answer_text(self, num):
        locator = (
            MainPageLocators.FAQ_ANSWER[0],
            MainPageLocators.FAQ_ANSWER[1].format(num=num),
        )
        self.wait.until(lambda d: self.find(locator).text != "")
        return self.get_text(locator)

    def click_order_button_top(self):
        self.click(MainPageLocators.ORDER_BUTTON_TOP)

    def click_order_button_bottom(self):
        self.click(MainPageLocators.ORDER_BUTTON_BOTTOM)

    def click_scooter_logo(self):
        self.click(MainPageLocators.SCOOTER_LOGO)

    def click_yandex_logo(self):
        self.click(MainPageLocators.YANDEX_LOGO)

    def switch_to_new_window(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])
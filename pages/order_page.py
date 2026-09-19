from selenium.webdriver.common.keys import Keys

from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):

    def fill_first_form(self, data):
        self.send_keys(OrderPageLocators.NAME_INPUT, data["name"])
        self.send_keys(OrderPageLocators.SURNAME_INPUT, data["surname"])
        self.send_keys(OrderPageLocators.ADDRESS_INPUT, data["address"])
        self.click(OrderPageLocators.METRO_INPUT)
        self.click((
            OrderPageLocators.METRO_OPTION[0],
            OrderPageLocators.METRO_OPTION[1].format(metro=data["metro"]),
        ))
        self.send_keys(OrderPageLocators.PHONE_INPUT, data["phone"])
        self.click(OrderPageLocators.NEXT_BUTTON)

    def fill_second_form(self, data):
        self.send_keys(OrderPageLocators.DATE_INPUT, data["date"])
        self.find(OrderPageLocators.DATE_INPUT).send_keys(Keys.ENTER)

        self.click(OrderPageLocators.RENT_DROPDOWN)
        self.click((
            OrderPageLocators.RENT_OPTION[0],
            OrderPageLocators.RENT_OPTION[1].format(rent=data["rent"]),
        ))
        self.click((
            OrderPageLocators.COLOR_CHECKBOX[0],
            OrderPageLocators.COLOR_CHECKBOX[1].format(color=data["color"]),
        ))
        self.send_keys(OrderPageLocators.COMMENT_INPUT, data["comment"])
        self.click(OrderPageLocators.ORDER_BUTTON)

    def confirm_order(self):
        self.click(OrderPageLocators.CONFIRM_BUTTON)

    def is_order_success(self):
        return self.is_visible(OrderPageLocators.SUCCESS_HEADER)
from selenium.webdriver.common.by import By


class OrderPageLocators:
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    METRO_OPTION = (By.XPATH, "//div[text()='{metro}']")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENT_DROPDOWN = (By.CLASS_NAME, "Dropdown-control")
    RENT_OPTION = (By.XPATH, "//div[contains(@class, 'Dropdown-option') and text()='{rent}']")
    COLOR_CHECKBOX = (By.ID, "{color}")
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "//div[contains(@class, 'Order_Buttons')]//button[text()='Заказать']")

    CONFIRM_BUTTON = (By.XPATH, "//div[contains(@class, 'Order_Modal')]//button[text()='Да']")
    SUCCESS_HEADER = (By.XPATH, "//div[contains(text(), 'Заказ оформлен')]")
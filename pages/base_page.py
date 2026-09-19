from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.base_locators import BaseLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def send_keys(self, locator, text):
        self.find(locator).send_keys(text)

    def get_text(self, locator):
        return self.find(locator).text

    def is_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).is_displayed()

    def accept_cookies(self):
        try:
            self.wait.until(EC.element_to_be_clickable(BaseLocators.COOKIE_BUTTON)).click()
        except Exception:
            pass
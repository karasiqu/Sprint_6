from selenium.webdriver.common.by import By


class MainPageLocators:
    FAQ_QUESTION = (By.ID, "accordion__heading-{num}")
    FAQ_ANSWER = (By.ID, "accordion__panel-{num}")

    ORDER_BUTTON_TOP = (By.XPATH, "//div[contains(@class, 'Header_Nav')]//button[text()='Заказать']")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "//div[contains(@class, 'Home_FinishButton')]//button[text()='Заказать']")

    YANDEX_LOGO = (By.XPATH, "//a[contains(@class, 'Header_LogoYandex')]")
    SCOOTER_LOGO = (By.XPATH, "//a[contains(@class, 'Header_LogoScooter')]")
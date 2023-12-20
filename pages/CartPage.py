from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class CartPage:

    BUTTON_PLACE_ORDER = (By.XPATH, "//*[@id='page-wrapper']/div/div[2]/button")

    def __init__(self, driver):
        self.driver: WebDriver = driver

    def click_place_order_button(self):
        web_element = self.driver.find_element(*self.BUTTON_PLACE_ORDER)
        web_element.click()

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class ProductPage:

    TITLE = (By.XPATH, "//*[@id='tbodyid']/h2")

    def __init__(self, driver):
        self.driver: WebDriver = driver

    def get_title(self):
        web_element = self.driver.find_element(*self.TITLE)
        return web_element.text

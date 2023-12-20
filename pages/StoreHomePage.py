from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class StoreHomePage:

    FIRST_ITEM = (By.XPATH, "//*[@id='tbodyid']/div[1]/div/div/h4/a")

    def __init__(self, driver):
        self.driver: WebDriver = driver

    def click_first_item(self):
        web_element = self.driver.find_element(*self.FIRST_ITEM)
        web_element.click()
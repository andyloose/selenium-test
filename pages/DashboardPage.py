from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class DashboardPage:

    MAIN_TITLE_DASHBOARD = (By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[1]/div[1]/span/h6")

    def __init__(self, driver):
        self.driver: WebDriver = driver

    def read_main_title_dashboard(self):
        web_element = self.driver.find_element(*self.MAIN_TITLE_DASHBOARD)
        return web_element.text




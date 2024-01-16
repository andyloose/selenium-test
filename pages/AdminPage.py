from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class AdminPage:

    INPUT_USERNAME = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div["
                                "1]/div/div[2]/input")
    BUTTON_SEARCH = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]")
    MESSAGE_NOT_RECORDS_FOUND = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/span")

    def __init__(self, driver):
        self.driver: WebDriver = driver

    def type_username(self, text):
        web_element = self.driver.find_element(*self.INPUT_USERNAME)
        web_element.send_keys(text)

    def click_button_search(self):
        web_element = self.driver.find_element(*self.BUTTON_SEARCH)
        web_element.click()

    def get_message_not_records_found(self):
        web_element = self.driver.find_element(*self.MESSAGE_NOT_RECORDS_FOUND)
        return web_element.text


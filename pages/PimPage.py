from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class PimPage:

    INPUT_EMPLOYEE_NAME = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div["
                                     "1]/div/div[2]/div/div/input")
    BUTTON_SEARCH = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]")
    MESSAGE_NO_RECORDS_FOUND = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/span")

    def __init__(self, driver):
        self.driver: WebDriver = driver

    def type_employee_name(self, text):
        web_element = self.driver.find_element(*self.INPUT_EMPLOYEE_NAME)
        web_element.send_keys(text)

    def click_button_search(self):
        web_element = self.driver.find_element(*self.BUTTON_SEARCH)
        web_element.click()

    def get_message_no_records_found(self):
        web_element = self.driver.find_element(*self.MESSAGE_NO_RECORDS_FOUND)
        return web_element.text

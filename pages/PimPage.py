from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class PimPage:
    INPUT_EMPLOYEE_NAME = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div["
                                     "1]/div/div[2]/div/div/input")
    BUTTON_SEARCH = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]")
    MESSAGE_NO_RECORDS_FOUND = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/span")
    MESSAGE_RECORD_FOUND = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/span")
    BUTTON_ADD = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[1]/button")
    BUTTON_SAVE = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]")
    MESSAGE_FIRST_NAME_REQUIRED = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div["
                                             "1]/div[1]/div/div/div[2]/div[1]/span")
    MESSAGE_LAST_NAME_REQUIRED = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div["
                                            "1]/div[1]/div/div/div[2]/div[3]/span")

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

    def get_message_record_found(self):
        web_element = self.driver.find_element(*self.MESSAGE_RECORD_FOUND)
        return web_element.text

    def click_button_add(self):
        web_element = self.driver.find_element(*self.BUTTON_ADD)
        web_element.click()

    def click_button_save(self):
        web_element = self.driver.find_element(*self.BUTTON_SAVE)
        web_element.click()

    def get_message_first_name_required(self):
        web_element = self.driver.find_element(*self.MESSAGE_FIRST_NAME_REQUIRED)
        return web_element.text

    def get_message_last_name_required(self):
        web_element = self.driver.find_element(*self.MESSAGE_LAST_NAME_REQUIRED)
        return web_element.text

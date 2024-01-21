from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class PersonalDetailsPage:
    MAIN_TITLE_PERSONAL_DETAILS = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/h6")
    INPUT_FIRST_NAME = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/input")
    INPUT_MIDDLE_NAME = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[1]/div/div/div[2]/div[2]/div[2]/input")
    INPUT_LAST_NAME = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[1]/div/div/div[2]/div[3]/div[2]/input")

    def __init__(self, driver):
        self.driver: WebDriver = driver

    def get_main_title_personal_details(self):
        web_element = self.driver.find_element(*self.MAIN_TITLE_PERSONAL_DETAILS)
        return web_element.text

    def get_input_first_name(self):
        web_element = self.driver.find_element(*self.INPUT_FIRST_NAME)
        return web_element.get_attribute("value")

    def get_input_middle_name(self):
        web_element = self.driver.find_element(*self.INPUT_MIDDLE_NAME)
        return web_element.get_attribute("value")

    def get_input_last_name(self):
        web_element = self.driver.find_element(*self.INPUT_LAST_NAME)
        return web_element.get_attribute("value")

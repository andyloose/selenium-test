from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class ResetPasswordPage:
    MAIN_TITLE_RESET_PASSWORD = (By.XPATH, "//*[@id='app']/div[1]/div[1]/div/form/div[2]/button[2]")
    INPUT_USERNAME = (By.XPATH, "//*[@id='app']/div[1]/div[1]/div/form/div[1]/div/div[2]/input")
    BUTTON_CANCEL = (By.XPATH, "//*[@id='app']/div[1]/div[1]/div/form/div[2]/button[1]")
    MESSAGE_ENTER_PASSWORD = (By.XPATH, "//*[@id='app']/div[1]/div[1]/div/form/p/p")
    BUTTON_RESET_PASSWORD = (By.XPATH, "//*[@id='app']/div[1]/div[1]/div/form/div[2]/button[2]")
    MESSAGE_ERROR = (By.XPATH, "//*[@id='app']/div[1]/div[1]/div/form/div[1]/div/span")
    MESSAGE_RESET_PASSWORD = (By.XPATH, "//*[@id='app']/div[1]/div[1]/div/h6")

    def __init__(self, driver):
        self.driver: WebDriver = driver

    def read_main_title_reset_password(self):
        web_element = self.driver.find_element(*self.MAIN_TITLE_RESET_PASSWORD)
        return web_element.text

    def type_username(self, text):
        web_element = self.driver.find_element(*self.INPUT_USERNAME)
        web_element.send_keys(text)

    def click_button_cancel(self):
        web_element = self.driver.find_element(*self.BUTTON_CANCEL)
        web_element.click()

    def get_enter_password_message(self):
        web_element = self.driver.find_element(*self.MESSAGE_ENTER_PASSWORD)
        return web_element.text

    def click_button_reset_password(self):
        web_element = self.driver.find_element(*self.BUTTON_RESET_PASSWORD)
        web_element.click()

    def get_error_message(self):
        web_element = self.driver.find_element(*self.MESSAGE_ERROR)
        return web_element.text

    def get_message_reset_password(self):
        web_element = self.driver.find_element(*self.MESSAGE_RESET_PASSWORD)
        return web_element.text

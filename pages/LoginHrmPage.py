from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class LoginHrmPage:
    INPUT_USERNAME = (By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input")
    INPUT_PASSWORD = (By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input")
    BUTTON_LOGIN = (By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button")
    MAIN_TITLE_LOGIN = (By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/h5")
    MESSAGE_INVALID_CREDENTIALS = (By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/p")
    LINK_FORGOT_PASSWORD = (By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[4]/p")

    def __init__(self, driver):
        self.driver: WebDriver = driver

    def type_username(self, text):
        web_element = self.driver.find_element(*self.INPUT_USERNAME)
        web_element.send_keys(text)

    def type_password(self, text):
        web_element = self.driver.find_element(*self.INPUT_PASSWORD)
        web_element.send_keys(text)

    def click_button_login(self):
        web_element = self.driver.find_element(*self.BUTTON_LOGIN)
        web_element.click()

    def read_main_title_login(self):
        web_element = self.driver.find_element(*self.MAIN_TITLE_LOGIN)
        return web_element.text

    def read_invalid_credential_message(self):
        web_element = self.driver.find_element(*self.MESSAGE_INVALID_CREDENTIALS)
        return web_element.text

    def click_link_forgot_password(self):
        web_element = self.driver.find_element(*self.LINK_FORGOT_PASSWORD)
        web_element.click()

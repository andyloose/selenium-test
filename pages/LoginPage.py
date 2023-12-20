from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class LoginPage:
    LINK_LOG_IN = (By.XPATH, "//*[@id='login2']")
    INPUT_USERNAME = (By.ID, "loginusername")
    INPUT_PASSWORD = (By.ID, "loginpassword")
    BUTTON_LOG_IN = (By.XPATH, "//*[@id='logInModal']/div/div/div[3]/button[2]")

    def __init__(self, driver):
        self.driver: WebDriver = driver

    def click_link_log_in(self):
        web_element = self.driver.find_element(*self.LINK_LOG_IN)
        web_element.click()

    def type_user_name(self, text):
        web_element = self.driver.find_element(*self.INPUT_USERNAME)
        web_element.send_keys(text)

    def type_password(self, text):
        web_element = self.driver.find_element(*self.INPUT_PASSWORD)
        web_element.send_keys(text)

    def click_button_log_in(self):
        web_element = self.driver.find_element(*self.BUTTON_LOG_IN)
        web_element.click()




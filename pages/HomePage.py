from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class HomePage:

    LINK_ENGLISH = (By.ID, "js-link-box-en")
    INPUT_SEARCH = (By.ID, "searchInput")
    BUTTON_MAGNIFYING_GLASS = (By.XPATH, "//*[@id='search-form']/fieldset/button")
    LINK_WELCOME_MESSAGE = (By.ID, "nameofuser")
    LINK_LOG_OUT = (By.ID, "logout2")
    LINK_LOG_IN = (By.ID, "login2")
    LINK_CART = (By.ID, "cartur")

    def __init__(self, driver):
        self.driver: WebDriver = driver

    def click_english_link(self):
        web_element = self.driver.find_element(*self.LINK_ENGLISH)
        web_element.click()

    def search(self, text):
        web_element: WebElement = self.driver.find_element(*self.INPUT_SEARCH)
        web_element.send_keys(text)
        web_element = self.driver.find_element(*self.BUTTON_MAGNIFYING_GLASS)
        web_element.click()

    def get_welcome_message(self):
        web_element: WebElement = self.driver.find_element(*self.LINK_WELCOME_MESSAGE)
        return web_element.text

    def click_link_log_out(self):
        web_element = self.driver.find_element(*self.LINK_LOG_OUT)
        web_element.click()

    def get_log_in_message(self):
        web_element: WebElement = self.driver.find_element(*self.LINK_LOG_IN)
        return web_element.text

    def click_link_cart(self):
        web_element = self.driver.find_element(*self.LINK_CART)
        web_element.click()


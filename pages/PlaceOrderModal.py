from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class PlaceOrderModal:

    INPUT_NAME = (By.ID, "name")
    INPUT_COUNTRY = (By.ID, "country")
    INPUT_CITY = (By.ID, "city")
    INPUT_CREDIT_CARD = (By.ID, "card")
    INPUT_MONTH = (By.ID, "month")
    INPUT_YEAR = (By.ID, "year")
    BUTTON_PURCHASE = (By.XPATH, "//*[@id='orderModal']/div/div/div[3]/button[2]")

    def __init__(self, driver):
        self.driver: WebDriver = driver

    def type_name(self, text):
        web_element = self.driver.find_element(*self.INPUT_NAME)
        web_element.send_keys(text)

    def type_country(self, text):
        web_element = self.driver.find_element(*self.INPUT_COUNTRY)
        web_element.send_keys(text)

    def type_city(self, text):
        web_element = self.driver.find_element(*self.INPUT_CITY)
        web_element.send_keys(text)

    def type_credit_card(self, text):
        web_element = self.driver.find_element(*self.INPUT_CREDIT_CARD)
        web_element.send_keys(text)

    def type_month(self, text):
        web_element = self.driver.find_element(*self.INPUT_MONTH)
        web_element.send_keys(text)

    def type_year(self, text):
        web_element = self.driver.find_element(*self.INPUT_YEAR)
        web_element.send_keys(text)

    def click_button_purchase(self):
        web_element = self.driver.find_element(*self.BUTTON_PURCHASE)
        web_element.click()


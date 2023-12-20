import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.HomePage import HomePage


class TestExample:

    def test_example01(self):
        driver = webdriver.Chrome()
        driver.get("http://www.wikipedia.org")
        time.sleep(2)
        home_page = HomePage(driver)
        home_page.search("aviones")

        time.sleep(2)
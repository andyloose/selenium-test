import time

from selenium import webdriver

from pages.CartPage import CartPage
from pages.HomePage import HomePage
from pages.LoginPage import LoginPage
from pages.PlaceOrderModal import PlaceOrderModal
from pages.ProductPage import ProductPage
from pages.StoreHomePage import StoreHomePage


class TestStore:

    def test_store(self):
        driver = webdriver.Chrome()
        driver.get("https://www.demoblaze.com/#")
        time.sleep(2)
        store_home_page = StoreHomePage(driver)
        store_home_page.click_first_item()
        time.sleep(3)

        product_page = ProductPage(driver)
        assert product_page.get_title() == "Samsung galaxy s6", "El titulo no coincide con el esperado"
        time.sleep(3)

    def test_log_in(self):
        driver = webdriver.Chrome()
        driver.get("https://www.demoblaze.com/#")
        time.sleep(2)
        login_page = LoginPage(driver)
        login_page.click_link_log_in()
        time.sleep(2)
        login_page.type_user_name("andrea22")
        login_page.type_password("134679")
        login_page.click_button_log_in()
        time.sleep(5)
        home_page = HomePage(driver)
        assert home_page.get_welcome_message() == "Welcome andrea22", "El mje de bienvenida no es el esperado"
        time.sleep(3)
        home_page = HomePage(driver)
        home_page.click_link_log_out()
        time.sleep(3)
        assert home_page.get_log_in_message() == "Log in", "El mje no es es el esperado"

    def test_click_cart_link(self):
        driver = webdriver.Chrome()
        driver.get("https://www.demoblaze.com/#")
        time.sleep(2)
        home_page = HomePage(driver)
        home_page.click_link_cart()
        time.sleep(2)
        cart_page = CartPage(driver)
        cart_page.click_place_order_button()
        time.sleep(2)
        place_order_modal = PlaceOrderModal(driver)
        place_order_modal.type_name("Andrea")
        time.sleep(2)
        place_order_modal.type_country("Argentina")
        time.sleep(2)
        place_order_modal.type_city("Posadas")
        time.sleep(2)
        place_order_modal.type_credit_card("1346794639178293")
        time.sleep(2)
        place_order_modal.type_month("07")
        time.sleep(2)
        place_order_modal.type_year("2025")
        time.sleep(2)
        place_order_modal.click_button_purchase()
        time.sleep(2)

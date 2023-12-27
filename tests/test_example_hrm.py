import time

from selenium import webdriver

from pages.DashboardPage import DashboardPage
from pages.LoginHrmPage import LoginHrmPage


class TestExampleHrm:

    def test_example_hrm(self):
        driver = webdriver.Chrome()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(2)
        login_hrm_page = LoginHrmPage(driver)
        assert login_hrm_page.read_main_title_login() == "Login", "Login button does not exist"

        login_hrm_page.type_username("Admin")
        login_hrm_page.type_password("admin123")
        login_hrm_page.click_button_login()
        time.sleep(5)
        dashboard_page = DashboardPage(driver)
        assert dashboard_page.read_main_title_dashboard()

    def test_wrong_password(self):
        driver = webdriver.Chrome()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(2)
        login_hrm_page = LoginHrmPage(driver)
        assert login_hrm_page.read_main_title_login() == "Login", "Login button does not exist"

        login_hrm_page.type_username("AdmiN")
        login_hrm_page.type_password("admin1234")
        login_hrm_page.click_button_login()
        time.sleep(5)
        assert login_hrm_page.read_invalid_credential_message() == "Invalid credentials", "Message not found"

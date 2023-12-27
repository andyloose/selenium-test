import time

from selenium import webdriver

from pages.DashboardPage import DashboardPage
from pages.LoginHrmPage import LoginHrmPage


class TestForgetPasswordHrm:

    def test_forget_password_hrm(self):
        driver = webdriver.Chrome()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(2)
        login_hrm_page = LoginHrmPage(driver)
        assert login_hrm_page.read_main_title_login() == "Login", "Login button does not exist"


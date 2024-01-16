import time

from selenium import webdriver

from pages.AdminPage import AdminPage
from pages.DashboardPage import DashboardPage
from pages.LoginHrmPage import LoginHrmPage


class TestAdminPageHrm:

    def test_admin_page_hrm(self):
        driver = webdriver.Chrome()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(10)
        login_hrm_page = LoginHrmPage(driver)
        login_hrm_page.type_username("Admin")
        login_hrm_page.type_password("admin123")
        login_hrm_page.click_button_login()
        time.sleep(10)

        dashboard_page = DashboardPage(driver)
        dashboard_page.click_link_admin()
        time.sleep(10)

        admin_page = AdminPage(driver)
        admin_page.type_username("Admin22")
        time.sleep(5)
        admin_page.click_button_search()
        time.sleep(5)
        assert admin_page.get_message_not_records_found() == "No Records Found", "No Records Found message not found"

import time

from selenium import webdriver

from pages.DashboardPage import DashboardPage
from pages.LoginHrmPage import LoginHrmPage
from pages.PimPage import PimPage


class TestPimPageHrm:

    def test_pim_page_error_assert(self):
        driver = webdriver.Chrome()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(5)
        login_hrm_page = LoginHrmPage(driver)
        login_hrm_page.type_username("Admin")
        login_hrm_page.type_password("admin123")
        login_hrm_page.click_button_login()
        time.sleep(5)

        dashboard_page = DashboardPage(driver)
        dashboard_page.click_link_pim()
        time.sleep(5)

        pim_page = PimPage(driver)
        pim_page.click_button_add()
        time.sleep(2)
        pim_page.click_button_save()
        time.sleep(2)
        assert pim_page.get_message_first_name_required() == "Required", "First Name Required message not found"
        assert pim_page.get_message_last_name_required() == "Required", "Last Name Required message not found"

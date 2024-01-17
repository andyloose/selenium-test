import time

from selenium import webdriver

from pages.DashboardPage import DashboardPage
from pages.LoginHrmPage import LoginHrmPage
from pages.PimPage import PimPage


class TestPimPageHrm:

    def test_pim_page_hrm(self):
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
        pim_page.type_employee_name("Raul")
        time.sleep(2)
        pim_page.click_button_search()
        time.sleep(2)
        assert pim_page.get_message_no_records_found() == "No Records Found", "No Records Found message not found"
        time.sleep(2)

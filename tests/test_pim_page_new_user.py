import time

from selenium import webdriver

from pages.DashboardPage import DashboardPage
from pages.LoginHrmPage import LoginHrmPage
from pages.PersonalDetailsPage import PersonalDetailsPage
from pages.PimPage import PimPage


class TestPimPageHrm:

    def test_pim_page_new_user(self):
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
        pim_page.type_first_name("Jon Bon")
        time.sleep(2)
        pim_page.type_middle_name("Singer")
        time.sleep(2)
        pim_page.type_last_name("Jovi")
        time.sleep(2)
        pim_page.click_button_save_new_user()
        time.sleep(10)

        personal_details_page = PersonalDetailsPage(driver)
        assert personal_details_page.get_main_title_personal_details() == "Personal Details", "Not in Personal Details Page"
        assert personal_details_page.get_input_first_name() == "Jon Bon", "Incorrect name"
        assert personal_details_page.get_input_middle_name() == "Singer", "Incorrect name"
        assert personal_details_page.get_input_last_name() == "Jovi", "Incorrect name"


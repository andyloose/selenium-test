import time

from selenium import webdriver

from pages.DashboardPage import DashboardPage
from pages.LoginHrmPage import LoginHrmPage


class TestExampleAssertDashboardPage:

    def test_assert_dashboard_page(self):
        driver = webdriver.Chrome()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(2)
        login_hrm_page = LoginHrmPage(driver)
        login_hrm_page.type_username("Admin")
        login_hrm_page.type_password("admin123")
        login_hrm_page.click_button_login()
        time.sleep(5)

        dashboard_page = DashboardPage(driver)
        assert dashboard_page.get_title_time_at_work() == "Time at Work"
        time.sleep(2)
        assert dashboard_page.get_title_my_actions() == "My Actions"
        time.sleep(2)
        assert dashboard_page.get_title_quick_launch() == "Quick Launch"
        time.sleep(2)
        assert dashboard_page.get_title_buzz_latest_posts() == "Buzz Latest Posts"
        time.sleep(2)
        assert dashboard_page.get_title_employees_on_leave_today() == "Employees on Leave Today"
        time.sleep(2)
        assert dashboard_page.get_title_employee_distribution_by_sub_unit() == "Employee Distribution by Sub Unit"
        time.sleep(2)
        assert dashboard_page.get_title_employee_distribution_by_location() == "Employee Distribution by Location"
        time.sleep(2)

        


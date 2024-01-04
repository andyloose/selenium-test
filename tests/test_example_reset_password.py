import time

from selenium import webdriver

from pages.LoginHrmPage import LoginHrmPage
from pages.ResetPasswordPage import ResetPasswordPage


class TestExampleResetPassword:

    def test_reset_password(self):
        driver = webdriver.Chrome()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(2)
        login_hrm_page = LoginHrmPage(driver)
        login_hrm_page.click_link_forgot_password()
        time.sleep(2)
        reset_password_page = ResetPasswordPage(driver)
        assert reset_password_page.read_main_title_reset_password() == "Reset Password", "Main title not found"

        reset_password_page.type_username("Luz")
        time.sleep(2)
        reset_password_page.click_button_cancel()
        time.sleep(2)
        login_hrm_page = LoginHrmPage(driver)
        assert login_hrm_page.read_main_title_login() == "Login", "Login button does not exist"

        login_hrm_page.click_link_forgot_password()
        time.sleep(2)
        reset_password_page = ResetPasswordPage(driver)
        assert reset_password_page.get_enter_password_message() == ("Please enter your username to identify your "
                                                                    "account to reset your password"), "error"
        reset_password_page.click_button_reset_password()
        time.sleep(2)
        assert reset_password_page.get_error_message() == "Required", "error"

        reset_password_page.type_username("Sophie")
        time.sleep(2)
        reset_password_page.click_button_reset_password()
        time.sleep(2)
        assert reset_password_page.get_message_reset_password() == "Reset Password link sent successfully", "error"




from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class DashboardPage:

    MAIN_TITLE_DASHBOARD = (By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[1]/div[1]/span/h6")
    TITLE_TIME_AT_WORK = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div/div[1]/div/p")
    TITLE_MY_ACTIONS = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div/div[1]/div/p")
    TITLE_QUICK_LAUNCH = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[3]/div/div[1]/div/p")
    TITLE_BUZZ_LATEST_POSTS = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[4]/div/div[1]/div/p")
    TITLE_EMPLOYEES_ON_LEAVE_TODAY = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[5]/div/div[1]/div/p")
    TITLE_EMPLOYEE_DISTRIBUTION_BY_SUB_UNIT = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[6]/div/div["
                                                         "1]/div/p")
    TITLE_EMPLOYEE_DISTRIBUTION_BY_LOCATION = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[7]/div/div["
                                                         "1]/div/p")

    def __init__(self, driver):
        self.driver: WebDriver = driver

    def read_main_title_dashboard(self):
        web_element = self.driver.find_element(*self.MAIN_TITLE_DASHBOARD)
        return web_element.text

    def get_title_time_at_work(self):
        web_element = self.driver.find_element(*self.TITLE_TIME_AT_WORK)
        return web_element.text

    def get_title_my_actions(self):
        web_element = self.driver.find_element(*self.TITLE_MY_ACTIONS)
        return web_element.text

    def get_title_quick_launch(self):
        web_element = self.driver.find_element(*self.TITLE_QUICK_LAUNCH)
        return web_element.text

    def get_title_buzz_latest_posts(self):
        web_element = self.driver.find_element(*self.TITLE_BUZZ_LATEST_POSTS)
        return web_element.text

    def get_title_employees_on_leave_today(self):
        web_element = self.driver.find_element(*self.TITLE_EMPLOYEES_ON_LEAVE_TODAY)
        return web_element.text

    def get_title_employee_distribution_by_sub_unit(self):
        web_element = self.driver.find_element(*self.TITLE_EMPLOYEE_DISTRIBUTION_BY_SUB_UNIT)
        return web_element.text

    def get_title_employee_distribution_by_location(self):
        web_element = self.driver.find_element(*self.TITLE_EMPLOYEE_DISTRIBUTION_BY_LOCATION)
        return web_element.text




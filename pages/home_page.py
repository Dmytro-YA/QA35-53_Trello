from selenium.webdriver.common.by import By

from pages.base_page import BasePage
import config
from pages.login_page import LoginPage


class HomePage(BasePage):
    LOGIN_LINK = (By.XPATH, "//a[@data-uuid='MJFtCCgVhXrVl7v9HA7EH_login']")

    def open(self)-> 'HomePage':
        self.driver.get(config.BASE_URL)
        return self

    def goto_login_page(self) -> 'LoginPage':
        self.click(self.LOGIN_LINK)
        return LoginPage(self.driver)


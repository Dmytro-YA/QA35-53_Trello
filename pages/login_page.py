from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from models.user import User
from pages.boards_page import BoardsPage


class LoginPage(BasePage):
    EMAIL = (By.XPATH, "//input[@data-testid='username']")
    CONTINUE_BUTTON = (By.ID, "login-submit")
    PASSWORD = (By.XPATH, "//input[@data-testid='password']")
    LOGIN_BUTTON = (By.XPATH, "//button[@data-testid='login-submit-idf-testid']")
    def login(self, user: User) -> BoardsPage:
        self.fill(self.EMAIL, user.email)
        self.click(self.CONTINUE_BUTTON)
        self.fill(self.PASSWORD, user.password)
        self.click(self.LOGIN_BUTTON)
        return BoardsPage(self.driver)


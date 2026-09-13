from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class BoardsPage(BasePage):

    CREATE_NEW_BOARD_BUTTON = (By.XPATH, "//button[@data-testid='create-board-tile']")
    CREATE_BOARD_BUTTON = (By.XPATH, "//button[@data-testid='create-board-button']")
    INPUT_BOARD_TITLE = (By.XPATH, "//input[@data-testid='create-board-title-input']")
    CREATE_SUBMIT_BUTTON = (By.XPATH, "//button[@data-testid='create-board-submit-button']")

    def create_new_board(self):
        self.click(self.CREATE_NEW_BOARD_BUTTON)
        self.click(self.CREATE_BOARD_BUTTON)
        self.fill(self.INPUT_BOARD_TITLE, "Test Board")
        self.click(self.CREATE_SUBMIT_BUTTON)





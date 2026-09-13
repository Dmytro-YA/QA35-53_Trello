

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import config
from models.user import User
from pages.home_page import HomePage


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--lang=en")
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)
    yield driver

    driver.quit()

@pytest.fixture
def user() -> User:
    return config.STANDART_USER

@pytest.fixture
def go_boards_page(driver, user):
    return HomePage(driver).open().goto_login_page().login(user)

import os

import allure
import pytest
from dotenv import load_dotenv
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.book_page import BookPage
from data.books import crime_dostoevsky
from utils import attach


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()

@pytest.fixture(scope='function')
def browser_setup():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.base_url = "https://www.litres.ru"
    login = os.getenv('LOGIN_SELENOID')
    password = os.getenv('PASSWORD_SELENOID')
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "128.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub",
        options=options
    )
    browser.config.driver = driver
    yield
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)
    browser.quit()


@pytest.fixture(scope='function')
def prefilled_favorites(browser_setup):
    book_page = BookPage()
    with allure.step(f"Открыть страницу книги \"{crime_dostoevsky.title}\""):
        book_page.open(crime_dostoevsky)
    with allure.step("Добавить книгу в \"Отложено\""):
        book_page.add_to_favorites()


@pytest.fixture(scope='function')
def prefilled_cart(browser_setup):
    book_page = BookPage()
    with allure.step(f"Открыть страницу книги \"{crime_dostoevsky.title}\""):
        book_page.open(crime_dostoevsky)
    with allure.step("Добавить книгу в корзину"):
        book_page.add_to_cart()
        book_page.close_dialog()

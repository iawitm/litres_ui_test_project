import allure
import pytest
from selene import browser

from pages.book_page import BookPage
from data.books import crime_dostoevsky
from utils import attach


@pytest.fixture(scope='function')
def browser_setup():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.base_url = "https://www.litres.ru"
    yield
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    #attach.add_video(browser)
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

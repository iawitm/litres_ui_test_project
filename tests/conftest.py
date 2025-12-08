import pytest
from selene import browser

from pages.book_page import BookPage
from data.books import crime_dostoevsky


@pytest.fixture(scope='function')
def browser_setup():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.base_url = "https://www.litres.ru"
    yield
    browser.quit()


@pytest.fixture(scope='function')
def prefilled_favorites(browser_setup):
    book_page = BookPage()
    book_page.open(crime_dostoevsky)
    book_page.add_to_favorites()


@pytest.fixture(scope='function')
def prefilled_cart(browser_setup):
    book_page = BookPage()
    book_page.open(crime_dostoevsky)
    book_page.add_to_cart()
    book_page.close_dialog()

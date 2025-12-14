import allure
from selene import browser, be, have

from data.books import Book


class MainPage:
    def open(self):
        with allure.step("Открыть главную страницу"):
            browser.open("/")

    def search_by_title(self, book: Book):
        with allure.step(f"Искать книгу по названию \"{book.title}\""):
            (browser.element('[data-testid="search__input"]').with_(timeout=60).should(be.visible).type(book.title)
             .press_enter())

    def book_should_have_title(self, book: Book):
        with allure.step(f"Проверить наличие названия \"{book.title}\" среди книг"):
            browser.element('[data-testid="art__title"]').with_(timeout=60).should(have.text(book.title))

    def empty_search_result_should_have_text(self):
        with allure.step(f"Проверить, что ничего не найдено"):
            browser.element('[data-testid="search-title__wrapper"]').with_(timeout=60).should(have.text
                                                                                              ("ничего не найдено"))

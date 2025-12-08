from selene import browser, be, have

from data.books import Book


class MainPage:
    def open(self):
        browser.open("/")

    def search_by_title(self, book: Book):
        browser.element('[data-testid="search__input"]').should(be.visible).type(book.title).press_enter()

    def book_should_have_title(self, book: Book):
        browser.element('[data-testid="art__title"]').should(have.text(book.title))

    def empty_search_result_should_have_text(self):
        browser.element('[data-testid="search-title__wrapper"]').should(have.text("ничего не найдено"))

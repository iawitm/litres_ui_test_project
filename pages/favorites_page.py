import allure
from selene import browser, be, have

from data.books import Book


class FavoritesPage:
    def open(self):
        with allure.step("Открыть страницу \"Отложено\""):
            browser.open("/my-books/liked/")

    def book_should_have_title(self, book: Book):
        with allure.step(f"Проверить в \"Отложено\" наличие книги с названием \"{book.title}\""):
            browser.element('[data-testid="art__title"]').with_(timeout=15).should(have.text(book.title))

    def book_should_have_author(self, book: Book):
        with allure.step(f"Проверить в \"Отложено\" автора книги \"{book.author}\""):
            browser.element('[data-testid="art__authorName--link"]').with_(timeout=15).should(have.text(book.author))

    def remove_book_from_favorites(self):
        with allure.step("Удалить книгу из \"Отложено\""):
            browser.element('//*[@data-testid="popover__baseElement"]/child::button[@aria-label="Меню"]').should(
                be.visible).click()
            browser.element('[data-testid="contextMenu__favorites--button"]').with_(timeout=15).should(
                be.visible).click()

    def empty_favorites_page_should_have_text(self):
        with allure.step("Проверить отсутствие книг в \"Отложено\""):
            browser.element('[data-testid="empty-state-content"]').with_(timeout=15).should(
                have.text('Здесь будет все, что вы отложите на потом'))

    def choose_book_from_recommendations(self):
        with allure.step("Нажать \"Выбрать книги\""):
            browser.element('[href="/recommend/"]').with_(timeout=15).should(be.visible).click()

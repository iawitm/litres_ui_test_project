from selene import browser, be, have

from data.books import Book


class FavoritesPage:
    def open(self):
        browser.open("/my-books/liked/")

    def book_should_have_title(self, book: Book):
        browser.element('[data-testid="art__title"]').should(have.text(book.title))

    def book_should_have_author(self, book: Book):
        browser.element('[data-testid="art__authorName--link"]').should(have.text(book.author))

    def remove_book_from_favorites(self):
        browser.element('//*[@data-testid="popover__baseElement"]/child::button[@aria-label="Меню"]').should(
            be.visible).click()
        browser.element('[data-testid="contextMenu__favorites--button"]').should(
            be.visible).click()

    def empty_favorites_page_should_have_text(self):
        browser.element('[data-testid="empty-state-content"]').should(
            have.text('Здесь будет все, что вы отложите на потом'))

    def choose_book_from_recommendations(self):
        browser.element('[href="/recommend/"]').should(be.visible).click()

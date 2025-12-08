from selene import browser, be, have

from data.books import Book


class CartPage:
    def open(self):
        browser.open("/my-books/cart/")

    def book_should_have_title(self, book: Book):
        browser.element('[data-testid="cart__bookCardTitle--wrapper"]').should(have.text(book.title))

    def book_should_have_author(self, book: Book):
        browser.element('[data-testid="cart__bookCardAuthor--wrapper"]').should(have.text(book.author))

    def make_an_order(self):
        browser.element('[data-testid="button__content"]').should(have.text("Перейти к покупке")).click()

    def unauthorized_user_should_have_dialog(self):
        browser.element('[data-testid="alert__description"]').should(have.text("Авторизуйтесь для покупки"))

    def press_delete_button(self):
        browser.element('[data-testid="cart__listDeleteButton"]').should(be.visible).click()

    def choose_delete_in_dialog(self):
        browser.element('[data-testid="cart__modalDeleteArt--button-primary"]').should(be.visible).click()

    def choose_delete_and_add_to_favorites_in_dialog(self):
        browser.element('[data-testid="cart__modalDeleteArt--button-secondary"]').should(be.visible).click()

    def empty_cart_should_have_text(self):
        browser.element('[data-testid="cart__emptyState--wrapper"]').should(have.text("Корзина пуста"))

    def press_favorite_button(self):
        browser.element('//div[@data-testid="icon_favorites"]').should(be.visible).click()

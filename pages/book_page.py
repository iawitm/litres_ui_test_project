from selene import browser, be, have, command
from selenium.webdriver import ActionChains

from data.books import Book


class BookPage:
    def open(self, book: Book):
        browser.open(f"/book/{book.url}")

    def add_to_favorites(self):
        browser.element('//*[@data-testid="wishlist__button"]/ancestor::button[@type="button"]').perform(
            command.js.click)

    def favorite_icon_should_be_exits(self):
        browser.element('[data-testid = "icon_favoritesFilled"]').with_(timeout=browser.config.timeout * 2).should(
            be.present)

    def add_to_cart(self):
        browser.element('[data-testid="book__addToCartButton"]').should(be.visible).click()

    def close_dialog(self):
        if browser.element('[data-testid="modal--content"]').with_(timeout=10).matching(be.visible):
            modal_el = browser.element('[data-testid="modal--close-button"]')()
            ActionChains(browser.driver).move_to_element(modal_el).click().perform()

    def cart_button_with_added_book_should_have_text(self):
        browser.element('[data-testid="book__goToCartButton"]') \
            .should(have.text('В корзине'))

import allure
from selene import browser, be, have

from data.books import Book
from utils import attach


class CartPage:
    def open(self):
        with allure.step("Открыть корзину"):
            browser.open("/my-books/cart/")

    def book_should_have_title(self, book: Book):
        with allure.step(f"Проверить в корзине наличие книги с названием \"{book.title}\""):
            browser.element('[data-testid="cart__bookCardTitle--wrapper"]').with_(timeout=60).should(have.text
                                                                                                     (book.title))

    def book_should_have_author(self, book: Book):
        with allure.step(f"Проверить в корзине автора книги \"{book.author}\""):
            browser.element('[data-testid="cart__bookCardAuthor--wrapper"]').with_(timeout=60).should(have.text
                                                                                                      (book.author))

    def make_an_order(self):
        with allure.step("Нажать \"Добавить в корзину\""):
            (browser.element('[data-testid="button__content"]').with_(timeout=60).should(have.text("Перейти к покупке"))
             .click())

    def unauthorized_user_should_have_dialog(self):
        with allure.step("Проверить наличие диалога о необходимости авторизоваться"):
            browser.element('[data-testid="alert__description"]').with_(timeout=60).should(have.text
                                                                                           ("Авторизуйтесь для покупки"))

    def press_delete_button(self):
        with allure.step("Нажать \"Удалить\""):
            browser.element('[data-testid="cart__listDeleteButton"]').with_(timeout=60).should(be.visible).click()

    def choose_delete_in_dialog(self):
        with allure.step("Нажать \"Удалить\" в диалоге"):
            (browser.element('[data-testid="cart__modalDeleteArt--button-primary"]').with_(timeout=60)
             .should(be.visible).click())

    def choose_delete_and_add_to_favorites_in_dialog(self):
        with allure.step("Нажать \"Отложить и удалить\" в диалоге"):
            (browser.element('[data-testid="cart__modalDeleteArt--button-secondary"]').with_(timeout=60)
             .should(be.visible).click())

    def empty_cart_should_have_text(self):
        with allure.step("Проверить, что корзина пустая"):
            browser.element('[data-testid="cart__emptyState--wrapper"]').with_(timeout=60).should(have.text
                                                                                                  ("Корзина пуста"))
            attach.add_screenshot(browser)

    def press_favorite_button(self):
        with allure.step("Нажать \"Отложить\""):
            browser.element('//div[@data-testid="icon_favorites"]').with_(timeout=60).should(be.visible).click()

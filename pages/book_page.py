import allure
from selene import browser, be, have, command
from selenium.webdriver import ActionChains

from data.books import Book
from utils import attach


class BookPage:
    def open(self, book: Book):
        with allure.step(f"Открыть страницу книги \"{book.title}\""):
            browser.open(f"/book/{book.url}")

    def add_to_favorites(self):
        with (allure.step("Добавить книгу в \"Отложено\"")):
            browser.element('//*[@data-testid="wishlist__button"]/ancestor::button[@type="button"]').with_(timeout=15
                                                                                                           ).perform(
                command.js.click)

    def favorite_icon_should_be_exits(self):
        with allure.step("Проверить факт добавления на странице книги"):
            browser.element('[data-testid = "icon_favoritesFilled"]').with_(timeout=15).should(
                be.present)
            attach.add_screenshot(browser)

    def add_to_cart(self):
        with allure.step("Добавить книгу в корзину из страницы книги"):
            browser.element('[data-testid="book__addToCartButton"]').with_(timeout=15).should(be.visible).click()

    def close_dialog(self):
        with allure.step("Закрыть всплывающий диалог (при наличии)"):
            if browser.element('[data-testid="modal--content"]').with_(timeout=15).matching(be.visible):
                modal_el = browser.element('[data-testid="modal--close-button"]')()
                ActionChains(browser.driver).move_to_element(modal_el).click().perform()

    def cart_button_with_added_book_should_have_text(self):
        with allure.step("Проверить факт добавления на странице книги"):
            browser.element('[data-testid="book__goToCartButton"]').with_(timeout=15) \
                .should(have.text('В корзине'))
            attach.add_screenshot(browser)

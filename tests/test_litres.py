import os
import time

from selene import browser, be, have, command
from selenium.webdriver import ActionChains


def test_positive_search(browser_setup):
    browser.open("/")

    browser.element('[data-testid="search__input"]').should(be.visible).type("Преступление и наказание").press_enter()
    browser.element('[data-testid="art__title"]').should(have.text("Преступление и наказание"))

def test_negative_search(browser_setup):
    browser.open("/")

    browser.element('[data-testid="search__input"]').should(be.visible).type("748247428748274").press_enter()
    browser.element('[data-testid="search-title__wrapper"]').should(have.text("ничего не найдено"))

def test_add_to_favorites(browser_setup):
    browser.open("/book/fedor-dostoevskiy/prestuplenie-i-nakazanie-72098209/")
    browser.element('//*[@data-testid="wishlist__button"]/ancestor::button[@type="button"]').perform(command.js.click)
    browser.element('[data-testid = "icon_favoritesFilled"]').with_(timeout=browser.config.timeout * 2).should(be.present)
    browser.open("/my-books/liked/")
    browser.element('[data-testid="art__title"]').should(have.text('Преступление и наказание'))
    browser.element('[data-testid="art__authorName--link"]').should(have.text('Федор Достоевский'))

def test_add_to_cart(browser_setup):
    browser.open("/book/fedor-dostoevskiy/prestuplenie-i-nakazanie-72098209/")
    browser.element('[data-testid="book__addToCartButton"]').should(be.visible).click()
    if browser.element('[data-testid="modal--content"]').with_(timeout=10).matching(be.visible):
        modal_el = browser.element('[data-testid="modal--close-button"]')() # получаем WebElement
        ActionChains(browser.driver).move_to_element(modal_el).click().perform()
    browser.element('[data-testid="book__goToCartButton"]') \
        .should(have.text('В корзине'))
    browser.open("/my-books/cart/")
    browser.element('[data-testid="cart__bookCardTitle--wrapper"]').should(have.text('Преступление и наказание'))
    browser.element('[data-testid="cart__bookCardAuthor--wrapper"]').should(have.text('Федор Достоевский'))

def test_remove_from_favorites(browser_setup):
    browser.open("/book/fedor-dostoevskiy/prestuplenie-i-nakazanie-72098209/")
    browser.element('//*[@data-testid="wishlist__button"]/ancestor::button[@type="button"]').perform(command.js.click)
    browser.element('[data-testid = "icon_favoritesFilled"]').with_(timeout=browser.config.timeout * 2).should(
        be.present)
    browser.open("/my-books/liked/")
    browser.element('//*[@data-testid="popover__baseElement"]/child::button[@aria-label="Меню"]').should(be.visible).click()
    browser.element('[data-testid="contextMenu__favorites--button"]').should(
        be.visible).click()
    browser.element('[data-testid="empty-state-content"]').should(have.text('Здесь будет все, что вы отложите на потом'))


def test_choose_favorite_from_recommendation(browser_setup):
    browser.open("/my-books/liked/")
    browser.element('[href="/recommend/"]').should(be.visible).click()
    browser.element('[data-testid="pageTitle"]').should(have.text("Рекомендации для вас"))

def test_buy_need_login(browser_setup):
    browser.open("/book/fedor-dostoevskiy/prestuplenie-i-nakazanie-72098209/")
    browser.element('[data-testid="book__addToCartButton"]').should(be.visible).click()
    if browser.element('[data-testid="modal--close-button"]').with_(timeout=10).matching(be.present):
        modal_el = browser.element('[data-testid="modal--close-button"]')()  # получаем WebElement
        time.sleep(0.5)
        ActionChains(browser.driver).move_to_element(modal_el).click().perform()
    browser.element('[data-testid="book__goToCartButton"]') \
        .should(have.text('В корзине'))
    browser.open("/my-books/cart/")
    browser.element('[data-testid="button__content"]').should(be.visible).click()
    browser.element('[data-testid="alert__description"]').should(have.text("Авторизуйтесь для покупки"))

def test_delete_from_cart(browser_setup):
    browser.open("/book/fedor-dostoevskiy/prestuplenie-i-nakazanie-72098209/")
    browser.element('[data-testid="book__addToCartButton"]').should(be.visible).click()
    if browser.element('[data-testid="modal--close-button"]').with_(timeout=10).matching(be.present):
        modal_el = browser.element('[data-testid="modal--close-button"]')()  # получаем WebElement
        time.sleep(0.5)
        ActionChains(browser.driver).move_to_element(modal_el).click().perform()
    browser.element('[data-testid="book__goToCartButton"]') \
        .should(have.text('В корзине'))
    browser.open("/my-books/cart/")
    browser.element('[data-testid="cart__listDeleteButton"]').should(be.visible).click()
    browser.element('[data-testid="cart__modalDeleteArt--button-primary"]').should(be.visible).click()
    browser.element('[data-testid="cart__emptyState--wrapper"]').should(have.text("Корзина пуста"))

def test_delete_from_cart_and_add_to_favorites(browser_setup):
    browser.open("/book/fedor-dostoevskiy/prestuplenie-i-nakazanie-72098209/")
    browser.element('[data-testid="book__addToCartButton"]').should(be.visible).click()
    if browser.element('[data-testid="modal--close-button"]').with_(timeout=10).matching(be.present):
        modal_el = browser.element('[data-testid="modal--close-button"]')()  # получаем WebElement
        time.sleep(0.5)
        ActionChains(browser.driver).move_to_element(modal_el).click().perform()
    browser.element('[data-testid="book__goToCartButton"]') \
        .should(have.text('В корзине'))
    browser.open("/my-books/cart/")
    browser.element('[data-testid="cart__listDeleteButton"]').should(be.visible).click()
    browser.element('[data-testid="cart__modalDeleteArt--button-secondary"]').should(be.visible).click()
    browser.element('[data-testid="cart__emptyState--wrapper"]').should(have.text("Корзина пуста"))
    browser.open("/my-books/liked/")
    browser.element('[data-testid="art__title"]').should(have.text("Преступление и наказание"))

def test_favorite_from_cart_without_delete(browser_setup):
    browser.open("/book/fedor-dostoevskiy/prestuplenie-i-nakazanie-72098209/")
    browser.element('[data-testid="book__addToCartButton"]').should(be.visible).click()
    if browser.element('[data-testid="modal--close-button"]').with_(timeout=10).matching(be.present):
        modal_el = browser.element('[data-testid="modal--close-button"]')()  # получаем WebElement
        time.sleep(0.5)
        ActionChains(browser.driver).move_to_element(modal_el).click().perform()
    browser.element('[data-testid="book__goToCartButton"]') \
        .should(have.text('В корзине'))
    browser.open("/my-books/cart/")
    browser.element('//div[@data-testid="icon_favorites"]').should(be.visible).click()
    browser.element('[data-testid="cart__bookCardTitle--wrapper"]').should(have.text('Преступление и наказание'))
    browser.element('[data-testid="cart__bookCardAuthor--wrapper"]').should(have.text('Федор Достоевский'))
    browser.open("/my-books/liked/")
    browser.element('[data-testid="art__title"]').should(have.text('Преступление и наказание'))
    browser.element('[data-testid="art__authorName--link"]').should(have.text('Федор Достоевский'))
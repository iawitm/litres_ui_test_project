import os
import time

from selene import browser, be, have, command
from selenium.webdriver import ActionChains


# Поиск успешный
# Поиск неуспешный
#
# Проверка читать/слушать
# Проверка отложить
# Корзина
#
# Отложить - Удалить
# Выбрать
#
# Корзина - Удалить
# Отложить


def test_positive_search(browser_setup):
    browser.open("/")

    browser.element('[data-testid="search__input"]').should(be.visible).type("Преступление и наказание").press_enter()
    browser.element('[data-testid="art__title"]').should(have.text("Преступление и наказание"))

def test_negative_search(browser_setup):
    browser.open("/")

    browser.element('[data-testid="search__input"]').should(be.visible).type("748247428748274").press_enter()
    browser.element('[data-testid="search-title__wrapper"]').should(have.text("ничего не найдено"))

def test_change_filter(browser_setup):
    browser.open("/book/fedor-dostoevskiy/prestuplenie-i-nakazanie-72098209/")
    browser.element('[data-testid="book-tabs-format__element_аудио"]').should(be.visible).click()
    #browser.element('//*[@id="book-card__wrapper"]/div[2]/div[3]/div[2]/div[3]/div/div[3]/button/div/div/div').with_(timeout=20).should(have.text("Слушать по подписке"))
    browser.element('[data-testid="book-sale-block__subscription-wrapper"]').with_(timeout=20).should(
        have.text("Слушать по подписке"))
    browser.element('[data-testid="book-tabs-format__element_текст"]').with_(timeout=browser.config.timeout * 2).should(be.visible).click()
    browser.element('[data-testid="book-sale-block__subscription-wrapper"]').with_(timeout=browser.config.timeout * 2).should(
         have.text("Читать по подписке"))

def test_add_to_favorites(browser_setup):
    browser.open("/book/fedor-dostoevskiy/prestuplenie-i-nakazanie-72098209/")
    browser.element('//*[@data-testid="wishlist__button"]/ancestor::button[@type="button"]').perform(command.js.click)
    browser.element('[data-testid = "icon_favoritesFilled"]').with_(timeout=browser.config.timeout * 2).should(be.present)

def test_add_to_cart(browser_setup):
    browser.open("/book/fedor-dostoevskiy/prestuplenie-i-nakazanie-72098209/")
    browser.element('[data-testid="book__addToCartButton"]').should(be.visible).click()
    if browser.element('[data-testid="modal--close-button"]').with_(timeout=10).matching(be.present):
        modal_el = browser.element('[data-testid="modal--close-button"]')() # получаем WebElement
        time.sleep(0.5)
        ActionChains(browser.driver).move_to_element(modal_el).click().perform()
        #browser.element('[data-testid="modal--close-button"]').click()
   # browser.element('//*[@data-testid="book__goToCartButton"]/child::div[@data-component="text-container"]').with_(timeout=browser.config.timeout).should(have.text("В корзине"))
    browser.element('[data-testid="book__goToCartButton"]') \
        .should(have.text('В корзине'))
    browser.open("/my-books/cart/")
    time.sleep(10)

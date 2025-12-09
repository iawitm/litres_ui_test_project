import allure

from data.books import crime_dostoevsky
from pages.book_page import BookPage
from pages.favorites_page import FavoritesPage
from pages.cart_page import CartPage
from utils import attach
from selene import browser


@allure.epic('Проверка страницы книги')
@allure.feature("Проверка действий на странице книги")
@allure.title("Добавление книги в \"Отложено\"")
@allure.tag('Регресс', 'WEB', 'Normal')
@allure.label('WEB')
@allure.severity('Normal')
def test_add_to_favorites(browser_setup):
    book_page = BookPage()
    favorites_page = FavoritesPage()
    with allure.step(f"Открыть страницу книги \"{crime_dostoevsky.title}\""):
        book_page.open(crime_dostoevsky)
    with allure.step("Добавить книгу в \"Отложено\""):
        book_page.add_to_favorites()
    with allure.step("Проверить факт добавления на странице книги"):
        book_page.favorite_icon_should_be_exits()
        attach.add_screenshot(browser)
    with allure.step("Перейти в \"Отложено\""):
        favorites_page.open()
    with allure.step(f"Проверить наличие книги с названием \"{crime_dostoevsky.title}\""):
        favorites_page.book_should_have_title(crime_dostoevsky)
    with allure.step(f"Проверить автора книги \"{crime_dostoevsky.author}\""):
        favorites_page.book_should_have_author(crime_dostoevsky)

@allure.epic('Проверка страницы книги')
@allure.feature("Проверка действий на странице книги")
@allure.title("Добавление книги в корзину")
@allure.tag('Регресс', 'WEB', 'Normal')
@allure.label('WEB')
@allure.severity('Normal')
def test_add_to_cart(browser_setup):
    book_page = BookPage()
    cart_page = CartPage()
    with allure.step(f"Открыть страницу книги \"{crime_dostoevsky.title}\""):
        book_page.open(crime_dostoevsky)
    with allure.step("Добавить книгу в корзину"):
        book_page.add_to_cart()
    with allure.step("Закрыть всплывающий диалог (при наличии)"):
        book_page.close_dialog()
    with allure.step("Проверить факт добавления на странице книги"):
        book_page.cart_button_with_added_book_should_have_text()
        attach.add_screenshot(browser)
    with allure.step("Перейти в \"Корзина\""):
        cart_page.open()
    with allure.step(f"Проверить наличие книги с названием \"{crime_dostoevsky.title}\""):
        cart_page.book_should_have_title(crime_dostoevsky)
    with allure.step(f"Проверить автора книги \"{crime_dostoevsky.author}\""):
        cart_page.book_should_have_author(crime_dostoevsky)
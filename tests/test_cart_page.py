import allure

from pages.cart_page import CartPage
from pages.favorites_page import FavoritesPage
from data.books import crime_dostoevsky
from utils import attach
from selene import browser


@allure.epic('Проверка страницы корзины')
@allure.feature("Проверка покупки книги")
@allure.title("Проверка необходимости авторизоваться перед покупкой")
@allure.tag('Регресс', 'WEB', 'Normal')
@allure.label('WEB')
@allure.severity('Normal')
def test_unauthorized_user_needs_login_to_buy(browser_setup, prefilled_cart):
    cart_page = CartPage()
    with allure.step("Открыть предзаполненную корзину"):
        cart_page.open()
    with allure.step("Нажать \"Добавить в корзину\""):
        cart_page.make_an_order()
    with allure.step("Проверить наличие диалога о необходимости авторизоваться"):
        cart_page.unauthorized_user_should_have_dialog()

@allure.epic('Проверка страницы корзины')
@allure.feature("Проверка удаления книги")
@allure.title("Удаление книги без добавления в избранное")
@allure.tag('Регресс', 'WEB', 'Normal')
@allure.label('WEB')
@allure.severity('Normal')
def test_delete_book_from_cart(browser_setup, prefilled_cart):
    cart_page = CartPage()
    with allure.step("Открыть предзаполненную корзину"):
        cart_page.open()
    with allure.step("Нажать \"Удалить\""):
        cart_page.press_delete_button()
    with allure.step("Нажать \"Удалить\" в диалоге"):
        cart_page.choose_delete_in_dialog()
    with allure.step("Проверить, что корзина пустая"):
        cart_page.empty_cart_should_have_text()


@allure.epic('Проверка страницы корзины')
@allure.feature("Проверка удаления книги")
@allure.title("Удаление книги с добавлением в избранное")
@allure.tag('Регресс', 'WEB', 'Normal')
@allure.label('WEB')
@allure.severity('Normal')
def test_delete_book_from_cart_and_add_to_favorites(browser_setup, prefilled_cart):
    cart_page = CartPage()
    favorites_page = FavoritesPage()
    with allure.step("Открыть предзаполненную корзину"):
        cart_page.open()
    with allure.step("Нажать \"Удалить\""):
        cart_page.press_delete_button()
    with allure.step("Нажать \"Отложить и удалить\" в диалоге"):
        cart_page.choose_delete_and_add_to_favorites_in_dialog()
    with allure.step("Проверить, что корзина пустая"):
        cart_page.empty_cart_should_have_text()
        attach.add_screenshot(browser)
    with allure.step("Перейти в \"Отложено\""):
        favorites_page.open()
    with allure.step(f"Проверить наличие книги с названием \"{crime_dostoevsky.title}\""):
        favorites_page.book_should_have_title(crime_dostoevsky)
    with allure.step(f"Проверить автора книги \"{crime_dostoevsky.author}\""):
        favorites_page.book_should_have_author(crime_dostoevsky)

@allure.epic('Проверка страницы корзины')
@allure.feature("Проверка добавления книги в \"Отложено\"")
@allure.title("Добавление книги в \"Отложено\" без удаления")
@allure.tag('Регресс', 'WEB', 'Normal')
@allure.label('WEB')
@allure.severity('Normal')
def test_favorite_book_from_cart_without_delete(browser_setup, prefilled_cart):
    cart_page = CartPage()
    favorites_page = FavoritesPage()
    with allure.step("Открыть предзаполненную корзину"):
        cart_page.open()
    with allure.step("Нажать \"Отложить\""):
        cart_page.press_favorite_button()
    with allure.step(f"Проверить в корзине наличие книги с названием \"{crime_dostoevsky.title}\""):
        cart_page.book_should_have_title(crime_dostoevsky)
    with allure.step(f"Проверить автора книги \"{crime_dostoevsky.author}\""):
        cart_page.book_should_have_author(crime_dostoevsky)
        attach.add_screenshot(browser)
    with allure.step("Перейти в \"Отложено\""):
        favorites_page.open()
    with allure.step(f"Проверить наличие книги с названием \"{crime_dostoevsky.title}\""):
        favorites_page.book_should_have_title(crime_dostoevsky)
    with allure.step(f"Проверить автора книги \"{crime_dostoevsky.author}\""):
        favorites_page.book_should_have_author(crime_dostoevsky)
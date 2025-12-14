import allure

from data.books import crime_dostoevsky
from pages.book_page import BookPage
from pages.favorites_page import FavoritesPage
from pages.cart_page import CartPage


@allure.epic('Проверка страницы книги')
@allure.feature("Проверка действий на странице книги")
class TestBookPage:
    @allure.title("Добавление книги в \"Отложено\"")
    @allure.tag('Регресс', 'WEB', 'Normal')
    @allure.label('WEB')
    @allure.severity('Normal')
    def test_add_to_favorites(self, browser_setup):
        book_page = BookPage()
        favorites_page = FavoritesPage()
        book_page.open(crime_dostoevsky)
        book_page.add_to_favorites()
        book_page.favorite_icon_should_be_exits()
        favorites_page.open()
        favorites_page.book_should_have_title(crime_dostoevsky)
        favorites_page.book_should_have_author(crime_dostoevsky)

    @allure.title("Добавление книги в корзину")
    @allure.tag('Регресс', 'WEB', 'Normal')
    @allure.label('WEB')
    @allure.severity('Normal')
    def test_add_to_cart(self, browser_setup):
        book_page = BookPage()
        cart_page = CartPage()
        book_page.open(crime_dostoevsky)
        book_page.add_to_cart()
        book_page.close_dialog()
        book_page.cart_button_with_added_book_should_have_text()
        cart_page.open()
        cart_page.book_should_have_title(crime_dostoevsky)
        cart_page.book_should_have_author(crime_dostoevsky)

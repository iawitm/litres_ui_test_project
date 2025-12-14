import allure

from pages.cart_page import CartPage
from pages.favorites_page import FavoritesPage
from data.books import crime_dostoevsky


@allure.epic('Проверка страницы корзины')
@allure.feature("Проверка действий на странице корзины")
class TestCartPage:
    @allure.title("Проверка необходимости авторизоваться перед покупкой")
    @allure.tag('Регресс', 'WEB', 'Normal')
    @allure.label('WEB')
    @allure.severity('Normal')
    def test_unauthorized_user_needs_login_to_buy(self, browser_setup, prefilled_cart):
        cart_page = CartPage()
        cart_page.open()
        cart_page.make_an_order()
        cart_page.unauthorized_user_should_have_dialog()

    @allure.title("Удаление книги без добавления в избранное")
    @allure.tag('Регресс', 'WEB', 'Normal')
    @allure.label('WEB')
    @allure.severity('Normal')
    def test_delete_book_from_cart(self, browser_setup, prefilled_cart):
        cart_page = CartPage()
        cart_page.open()
        cart_page.press_delete_button()
        cart_page.choose_delete_in_dialog()
        cart_page.empty_cart_should_have_text()

    @allure.title("Удаление книги с добавлением в избранное")
    @allure.tag('Регресс', 'WEB', 'Normal')
    @allure.label('WEB')
    @allure.severity('Normal')
    def test_delete_book_from_cart_and_add_to_favorites(self, browser_setup, prefilled_cart):
        cart_page = CartPage()
        favorites_page = FavoritesPage()
        cart_page.open()
        cart_page.press_delete_button()
        cart_page.choose_delete_and_add_to_favorites_in_dialog()
        cart_page.empty_cart_should_have_text()
        favorites_page.open()
        favorites_page.book_should_have_title(crime_dostoevsky)
        favorites_page.book_should_have_author(crime_dostoevsky)

    @allure.title("Добавление книги в \"Отложено\" без удаления")
    @allure.tag('Регресс', 'WEB', 'Normal')
    @allure.label('WEB')
    @allure.severity('Normal')
    def test_favorite_book_from_cart_without_delete(self, browser_setup, prefilled_cart):
        cart_page = CartPage()
        favorites_page = FavoritesPage()
        cart_page.open()
        cart_page.press_favorite_button()
        cart_page.book_should_have_title(crime_dostoevsky)
        cart_page.book_should_have_author(crime_dostoevsky)
        favorites_page.open()
        favorites_page.book_should_have_title(crime_dostoevsky)
        favorites_page.book_should_have_author(crime_dostoevsky)

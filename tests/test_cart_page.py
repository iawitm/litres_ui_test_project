from pages.cart_page import CartPage
from pages.favorites_page import FavoritesPage
from data.books import crime_dostoevsky


def test_unauthorized_user_needs_login_to_buy(browser_setup, prefilled_cart):
    cart_page = CartPage()
    cart_page.open()
    cart_page.make_an_order()
    cart_page.unauthorized_user_should_have_dialog()

def test_delete_book_from_cart(browser_setup, prefilled_cart):
    cart_page = CartPage()
    cart_page.open()
    cart_page.press_delete_button()
    cart_page.choose_delete_in_dialog()
    cart_page.empty_cart_should_have_text()

def test_delete_book_from_cart_and_add_to_favorites(browser_setup, prefilled_cart):
    cart_page = CartPage()
    favorites_page = FavoritesPage()
    cart_page.open()
    cart_page.press_delete_button()
    cart_page.choose_delete_and_add_to_favorites_in_dialog()
    cart_page.empty_cart_should_have_text()
    favorites_page.open()
    favorites_page.book_should_have_title(crime_dostoevsky)
    favorites_page.book_should_have_author(crime_dostoevsky)

def test_favorite_book_from_cart_without_delete(browser_setup, prefilled_cart):
    cart_page = CartPage()
    favorites_page = FavoritesPage()
    cart_page.open()
    cart_page.press_favorite_button()
    cart_page.book_should_have_title(crime_dostoevsky)
    cart_page.book_should_have_author(crime_dostoevsky)
    favorites_page.open()
    favorites_page.book_should_have_title(crime_dostoevsky)
    favorites_page.book_should_have_author(crime_dostoevsky)
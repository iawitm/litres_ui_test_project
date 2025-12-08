from data.books import crime_dostoevsky
from pages.book_page import BookPage
from pages.favorites_page import FavoritesPage
from pages.cart_page import CartPage

def test_add_to_favorites(browser_setup):
    book_page = BookPage()
    favorites_page = FavoritesPage()
    book_page.open(crime_dostoevsky)
    book_page.add_to_favorites()
    book_page.favorite_icon_should_be_exits()
    favorites_page.open()
    favorites_page.book_should_have_title(crime_dostoevsky)
    favorites_page.book_should_have_author(crime_dostoevsky)


def test_add_to_cart(browser_setup):
    book_page = BookPage()
    cart_page = CartPage()
    book_page.open(crime_dostoevsky)
    book_page.add_to_cart()
    book_page.close_dialog()
    book_page.cart_button_with_added_book_should_have_text()
    cart_page.open()
    cart_page.book_should_have_title(crime_dostoevsky)
    cart_page.book_should_have_author(crime_dostoevsky)
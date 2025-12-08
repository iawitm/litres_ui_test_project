from data.books import crime_dostoevsky, invalid_book
from pages.main_page import MainPage

def test_positive_search(browser_setup):
    main_page = MainPage()
    main_page.open()
    main_page.search_by_title(crime_dostoevsky)
    main_page.book_should_have_title(crime_dostoevsky)

def test_negative_search(browser_setup):
    main_page = MainPage()
    main_page.open()
    main_page.search_by_title(invalid_book)
    main_page.empty_search_result_should_have_text()
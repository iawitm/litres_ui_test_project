import allure

from data.books import crime_dostoevsky, invalid_book
from pages.main_page import MainPage


@allure.epic('Проверка главной страницы')
@allure.feature("Проверка поиска")
class TestMainPage:
    @allure.title("Поиск существующей книги по ее названию")
    @allure.tag('Регресс', 'WEB', 'Normal')
    @allure.label('WEB')
    @allure.severity('Normal')
    def test_positive_search(self, browser_setup):
        main_page = MainPage()
        main_page.open()
        main_page.search_by_title(crime_dostoevsky)
        main_page.book_should_have_title(crime_dostoevsky)

    @allure.title("Поиск несуществующей книги")
    @allure.tag('Регресс', 'WEB', 'Normal')
    @allure.label('WEB')
    @allure.severity('Normal')
    def test_negative_search(self, browser_setup):
        main_page = MainPage()
        main_page.open()
        main_page.search_by_title(invalid_book)
        main_page.empty_search_result_should_have_text()

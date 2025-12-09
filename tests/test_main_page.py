import allure

from data.books import crime_dostoevsky, invalid_book
from pages.main_page import MainPage


@allure.epic('Проверка главной страницы')
@allure.feature("Проверка поиска")
@allure.title("Поиск существующей книги по ее названию")
@allure.tag('Регресс', 'WEB', 'Normal')
@allure.label('WEB')
@allure.severity('Normal')
def test_positive_search(browser_setup):
    main_page = MainPage()
    with allure.step("Открыть главную страницу"):
        main_page.open()
    with allure.step(f"Искать книгу по названию \"{crime_dostoevsky.title}\""):
        main_page.search_by_title(crime_dostoevsky)
    with allure.step(f"Проверить наличие названия \"{crime_dostoevsky.title}\" среди книг"):
        main_page.book_should_have_title(crime_dostoevsky)

@allure.epic('Проверка главной страницы')
@allure.feature("Проверка поиска")
@allure.title("Поиск несуществующей книги")
@allure.tag('Регресс', 'WEB', 'Normal')
@allure.label('WEB')
@allure.severity('Normal')
def test_negative_search(browser_setup):
    main_page = MainPage()
    with allure.step("Открыть главную страницу"):
        main_page.open()
    with allure.step(f"Искать книгу по названию \"{invalid_book.title}\""):
        main_page.search_by_title(invalid_book)
    with allure.step(f"Проверить, что ничего не найдено"):
        main_page.empty_search_result_should_have_text()

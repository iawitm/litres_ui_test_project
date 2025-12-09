import allure

from pages.favorites_page import FavoritesPage
from pages.recommendation_page import RecommendationPage

@allure.epic('Проверка страницы \"Отложено\"')
@allure.feature("Проверка действий на странице \"Отложено\"")
@allure.title("Удаление книги из \"Отложено\"")
@allure.tag('Регресс', 'WEB', 'Normal')
@allure.label('WEB')
@allure.severity('Normal')
def test_remove_from_favorites(browser_setup, prefilled_favorites):
    favorites_page = FavoritesPage()
    with allure.step("Открыть предзаполненную страницу \"Отложено\""):
        favorites_page.open()
    with allure.step("Удалить книгу из \"Отложено\""):
        favorites_page.remove_book_from_favorites()
    with allure.step("Проверить отсутствие книг в \"Отложено\""):
        favorites_page.empty_favorites_page_should_have_text()

@allure.epic('Проверка страницы \"Отложено\"')
@allure.feature("Проверка действий на странице \"Отложено\"")
@allure.title("Выбор книги из \"Отложено\" ведет на страницу рекомендаций")
@allure.tag('Регресс', 'WEB', 'Normal')
@allure.label('WEB')
@allure.severity('Normal')
def test_choose_book_leads_to_recommendation_page(browser_setup):
    favorites_page = FavoritesPage()
    recommendation_page = RecommendationPage()
    with allure.step("Открыть страницу \"Отложено\""):
        favorites_page.open()
    with allure.step("Нажать \"Выбрать книги\""):
        favorites_page.choose_book_from_recommendations()
    with allure.step("Проверить открытие страницы \"Рекомендации для вас\""):
        recommendation_page.page_should_have_text()


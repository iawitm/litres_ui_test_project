import allure

from pages.favorites_page import FavoritesPage
from pages.recommendation_page import RecommendationPage


@allure.epic('Проверка страницы \"Отложено\"')
@allure.feature("Проверка действий на странице \"Отложено\"")
class TestFavoritesPage:
    @allure.title("Удаление книги из \"Отложено\"")
    @allure.tag('Регресс', 'WEB', 'Normal')
    @allure.label('WEB')
    @allure.severity('Normal')
    def test_remove_from_favorites(self, browser_setup, prefilled_favorites):
        favorites_page = FavoritesPage()
        favorites_page.open()
        favorites_page.remove_book_from_favorites()
        favorites_page.empty_favorites_page_should_have_text()

    @allure.title("Выбор книги из \"Отложено\" ведет на страницу рекомендаций")
    @allure.tag('Регресс', 'WEB', 'Normal')
    @allure.label('WEB')
    @allure.severity('Normal')
    def test_choose_book_leads_to_recommendation_page(self, browser_setup):
        favorites_page = FavoritesPage()
        recommendation_page = RecommendationPage()
        favorites_page.open()
        favorites_page.choose_book_from_recommendations()
        recommendation_page.page_should_have_text()

from pages.favorites_page import FavoritesPage
from pages.recommendation_page import RecommendationPage


def test_remove_from_favorites(browser_setup, prefilled_favorites):
    favorites_page = FavoritesPage()
    favorites_page.open()
    favorites_page.remove_book_from_favorites()
    favorites_page.empty_favorites_page_should_have_text()

def test_choose_book_leads_to_recommendation_page(browser_setup):
    favorites_page = FavoritesPage()
    recommendation_page = RecommendationPage()
    favorites_page.open()
    favorites_page.choose_book_from_recommendations()
    recommendation_page.page_should_have_text()


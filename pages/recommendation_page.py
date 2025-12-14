import allure
from selene import browser, have


class RecommendationPage:
    def page_should_have_text(self):
        with allure.step("Проверить открытие страницы \"Рекомендации для вас\""):
            browser.element('[data-testid="pageTitle"]').with_(timeout=60).should(have.text("Рекомендации для вас"))

from selene import browser, have


class RecommendationPage:
    def page_should_have_text(self):
        browser.element('[data-testid="pageTitle"]').should(have.text("Рекомендации для вас"))

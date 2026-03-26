from playwright.sync_api import Page

class BlogHomePage:
    def __init__(self, page: Page):
        self.page = page
        self.base_url = "https://blog.agibank.com.br"

        self.search_icon = "a.astra-search-icon[aria-label='Search button']"
        # Campo de busca (id = search-field)
        self.search_input = "input#search-field"
        # Cada resultado de artigo na página de busca
        self.search_result_item = "main.site-main article.post"
        # Seção de 'nada encontrado' quando a busca não retorna posts
        self.no_results_message = "section.no-results.not-found"

    def open(self):
        self.page.goto(self.base_url)

    def open_search(self):
        self.page.click(self.search_icon)

    def search(self, term: str):
        self.page.fill(self.search_input, term)
        self.page.press(self.search_input, "Enter")

    def get_results_count(self) -> int:
        return self.page.locator(self.search_result_item).count()

    def has_no_results_message(self) -> bool:
        locator = self.page.locator(self.no_results_message)
        return locator.first.is_visible() if locator.count() > 0 else False
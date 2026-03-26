from playwright.sync_api import Page, expect

class BlogHomePage:
    def __init__(self, page: Page):
        self.page = page
        self.base_url = "https://blog.agibank.com.br"

        # Ajuste os seletores inspecionando o DOM no navegador
        self.search_icon = "button[aria-label='Buscar'], .search-toggle, .icon-search"
        self.search_input = "input[type='search'], input[name='s']"
        self.search_result_item = "article, .post, .card-post"
        self.no_results_message = "text='Nenhum resultado encontrado', .no-results"

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
        return self.page.locator(self.no_results_message).first.is_visible()
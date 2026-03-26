from playwright.sync_api import expect

def test_search_returns_results(blog_home):
    search_term = "empréstimo"

    blog_home.open_search()
    blog_home.search(search_term)

    count = blog_home.get_results_count()
    assert count > 0, "Esperava ao menos 1 resultado de busca"

    # Exemplo simples de verificação de texto no primeiro resultado
    first_result = blog_home.page.locator(blog_home.search_result_item).first
    expect(first_result).to_be_visible()
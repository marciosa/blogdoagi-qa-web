from playwright.sync_api import expect

def test_search_returns_results(blog_home):
    search_term = "emprestimo"  # termo que deve retornar resultados

    blog_home.open_search()
    blog_home.search(search_term)

    # Verifica que HÁ cards de resultado
    count = blog_home.get_results_count()
    assert count > 0, f"Nenhum resultado encontrado para termo '{search_term}'. Esperava ao menos 1."

    # O primeiro resultado deve estar visível
    first_result = blog_home.page.locator(blog_home.search_result_item).first
    expect(first_result).to_be_visible()

    # Opcional: verificar que o termo aparece no conteúdo (mais robusto)
    # first_result_text = first_result.inner_text()
    # assert search_term.lower() in first_result_text.lower(), "Termo de busca não encontrado no primeiro resultado"
def test_search_no_results(blog_home):
    search_term = "asdfghjklteste123"

    blog_home.open_search()
    blog_home.search(search_term)

    # Verifica que NÃO há cards de resultado
    count = blog_home.get_results_count()
    assert count == 0, f"Encontrados {count} resultados inesperados para termo '{search_term}'"

    # E que a mensagem de 'nenhum resultado' está visível
    no_results_visible = blog_home.has_no_results_message()
    assert no_results_visible, "Esperava mensagem de 'nenhum resultado' visível"
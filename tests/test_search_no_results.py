def test_search_no_results(blog_home):
    search_term = "asdfghjklteste123"

    blog_home.open_search()
    blog_home.search(search_term)

    # Duas opções de validação: mensagem de 'nenhum resultado' ou zero cards
    if blog_home.has_no_results_message():
        assert True
    else:
        count = blog_home.get_results_count()
        assert count == 0, "Esperava 0 resultados para termo inexistente"
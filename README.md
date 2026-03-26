# Teste Técnico QA – Web (Blog do Agi)

Este projeto contém a automação dos cenários de busca de artigos no Blog do Agi, utilizando **Python + Playwright + Pytest**.

## Cenários automatizados

1. **Busca com resultados válidos**  
   - Dado que estou na página inicial do Blog do Agi  
   - Quando realizo uma busca por um termo existente (ex.: "empréstimo")  
   - Então devo visualizar uma lista de artigos relacionados ao termo pesquisado

2. **Busca sem resultados**  
   - Dado que estou na página inicial do Blog do Agi  
   - Quando realizo uma busca por um termo inexistente  
   - Então devo visualizar uma mensagem indicando ausência de resultados ou nenhum card de artigo na listagem

## Requisitos

- Python 3.11+
- pip
- Git
- Navegador (Playwright instala os necessários automaticamente)

Testado em Linux, Windows e macOS.

## Passos para configuração

```bash
git clone https://github.com/SEU_USUARIO/blogdoagi-qa-web.git
cd blogdoagi-qa-web

python -m venv .venv
# Linux/Mac
source .venv/bin/activate
# Windows (PowerShell)
# .venv\Scripts\Activate.ps1

pip install -r requirements.txt
playwright install
```

## Como executar os testes

```bash
pytest -v
```

Os testes rodam em modo headless por padrão.  
Para rodar em modo com UI, altere o fixture `browser` em `conftest.py` para `headless=False`.

## Estrutura do projeto

```text
blogdoagi-qa-web/
  ├─ tests/
  │   ├─ test_search_valid.py
  │   └─ test_search_no_results.py
  ├─ pages/
  │   └─ blog_home_page.py
  ├─ conftest.py
  ├─ requirements.txt
  └─ README.md
```

## Execução em CI (GitHub Actions)

Um workflow de exemplo está disponível em `.github/workflows/ci.yml`, permitindo que os testes sejam executados automaticamente a cada push.
import sys
from tech_news.analyzer.ratings import top_5_categories
from tech_news.analyzer.search_engine import (
    search_by_category,
    search_by_date,
    search_by_title,
)
from tech_news.scraper import get_tech_news


def analyzer_menu():
    inputs = input(
        "Selecione uma das opções a seguir:\n"
        " 0 - Popular o banco com notícias;\n"
        " 1 - Buscar notícias por título;\n"
        " 2 - Buscar notícias por data;\n"
        " 3 - Buscar notícias por categoria;\n"
        " 4 - Listar top 5 categorias;\n"
        " 5 - Sair.\n"
    )

    result = {
        "0": get_quantity,
        "1": get_title,
        "2": get_data,
        "3": get_category,
        "4": get_top_5,
        "5": bye_app,
    }

    try:
        result[inputs]()
    except KeyError:
        sys.stderr.write("Opção inválida\n")


def get_quantity():
    quantity = input("Digite quantas notícias serão buscadas:")
    print(get_tech_news(int(quantity)))


def get_title():
    title = input("Digite o título:")
    print(search_by_title(title))


def get_data():
    date = input("Digite a data no formato aaaa-mm-dd:")
    print(search_by_date(date))


def get_category():
    category = input("Digite a categoria:")
    print(search_by_category(category))


def get_top_5():
    print(top_5_categories())


def bye_app():
    print("Encerrando script\n")

import datetime
from tech_news.database import search_news


# Requisito 7
def search_by_title(title):
    query = {"title": {"$regex": title, "$options": "i"}}

    return [(news["title"], news["url"]) for news in search_news(query)]


# Requisito 8
def search_by_date(date):
    try:
        date = datetime.date.fromisoformat(date).strftime("%d/%m/%Y")
    except ValueError:
        raise ValueError("Data inválida")

    query = {"timestamp": date}

    return [(news["title"], news["url"]) for news in search_news(query)]


# Requisito 9
def search_by_category(category):
    query = {"category": {"$regex": category, "$options": "i"}}

    return [(news["title"], news["url"]) for news in search_news(query)]

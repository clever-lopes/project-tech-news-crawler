# import datetime
from tech_news.database import search_news


# Requisito 7
def search_by_title(title):
  query = {"title": {"$regex": title, "$options": "i"}}

  return [(news["title"], news["url"]) for news in search_news(query)]

# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""

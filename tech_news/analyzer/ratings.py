from tech_news.database import find_news
from collections import Counter


# Requisito 10
def top_5_categories():
    data = find_news()
    category_list = [news["category"] for news in data]

    counter = Counter(category_list)
    categories = sorted(counter.items(), key=lambda x: (-x[1], x[0]))

    result = [category[0] for category in categories]
    return result[:5]

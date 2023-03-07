import time
import requests
from parsel import Selector
from requests.exceptions import ReadTimeout
from sorcery import dict_of


# Requisito 1
def fetch(url):
    try:
        res = requests.get(url, headers={"user-agent": "Fake user-agent"})
        time.sleep(1)
    except ReadTimeout:
        return None

    if res.status_code != 200:
        return None

    return res.text


# Requisito 2
def scrape_updates(html_content):
    return Selector(text=html_content).css("h2 > a::attr(href)").getall()


# Requisito 3
def scrape_next_page_link(html_content):
    return Selector(text=html_content).css("a.next::attr(href)").get()


# Requisito 4
def scrape_news(html_content):
    selector = Selector(html_content)
    url = selector.css("link[rel=canonical] ::attr(href)").get()
    title = selector.css("h1.entry-title ::text").get()
    timestamp = selector.css("li.meta-date ::text").get()
    writer = selector.css("li.meta-author > span.author > a ::text").get()
    reading_time = selector.css("li.meta-reading-time ::text").get()
    summary = "".join(
        selector.css(".entry-content > p:first-of-type ::text").getall()
    ).strip()
    category = selector.css("a.category-style > span.label ::text").get()
    news = dict_of(
        url,
        title,
        timestamp,
        writer,
        reading_time,
        summary,
        category,
    )
    return news


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""

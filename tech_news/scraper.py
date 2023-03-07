import time
import requests
from parsel import Selector
from requests.exceptions import ReadTimeout
from tech_news.database import create_news


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
    requests = Selector(html_content)
    news = {
        "url": requests.css("link[rel=canonical] ::attr(href)").get(),
        "title": requests.css("h1.entry-title ::text").get().strip(),
        "timestamp": requests.css("li.meta-date ::text").get(),
        "writer": requests.css(
            "li.meta-author > span.author > a ::text"
        ).get(),
        "reading_time": int(
            requests.css("li.meta-reading-time ::text")
            .get()
            .replace("minutos de leitura", "")
        ),
        "summary": "".join(
            requests.css(".entry-content > p:first-of-type ::text").getall()
        ).strip(),
        "category": requests.css("a.category-style > span.label ::text").get(),
    }
    return news


# Requisito 5
def get_tech_news(amount):
    BASE_URL = "https://blog.betrybe.com/"
    fetch_url = fetch(BASE_URL)
    news_urls = scrape_updates(fetch_url)
    # 12 news per page
    while len(news_urls) < amount:
        fetch_url = fetch(scrape_next_page_link(fetch_url))
        news_urls += scrape_updates(fetch_url)

    new_list = [scrape_news(fetch(url)) for url in news_urls[:amount]]
    create_news(new_list)
    return new_list 

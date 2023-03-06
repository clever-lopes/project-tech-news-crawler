import time
import requests
from parsel import Selector
from requests.exceptions import ReadTimeout


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
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""

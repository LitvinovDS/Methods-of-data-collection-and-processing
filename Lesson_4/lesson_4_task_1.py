import requests
import time
from datetime import datetime
from pprint import pprint
from pymongo import MongoClient
from lxml import lxml

headers = {
    'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/88.0.4324.96 Safari/537.36"
}

MONGO_URL = "127.0.0.1:27017"
MONGO_DB = "News"
client = MongoClient(MONGO_URL)
db = client[MONGO_DB]


def get_news_Lenta():
    url = "https://lenta.ru/"
    r = requests.get(url, headers)
    dom = html.fromstring(r.text)
    item_xpath = '//section[@class="row b-top7-for-main js-top-seven"]//div[contains(@class, "item")]'
    items = dom.xpath(item_xpath)
    info = list()
    for item in items:
        info_item = dict()
        xpath_item_name = ".//a/text()"

        info["source"] = "Lenta.ru"
        info["news_name"] = item.xpath(xpath_item_name)[0].replace('\xa0', '')
        info["news_url"] = url + item.xpath(".//a/@href")[0]
        info["news_datetime"] = item.xpath(".//a/time/@datetime")[0]
     return info
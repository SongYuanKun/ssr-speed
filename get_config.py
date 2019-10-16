import logging
import re
from urllib.request import ProxyHandler, build_opener

from bs4 import BeautifulSoup

logging.basicConfig(level=logging.INFO)

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'cookie': '__cfduid=d15534a5fedadd9770b7b73227bcad2b61570850521; _ga=GA1.2.1193099936.1570850527; PHPSESSID=9fp7gag838u40fjc106lerpvcq; _gid=GA1.2.349119984.1571230574; _gat_gtag_UA_138692554_1=1',
    'pragma': 'no-cache',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': 1,
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
}
proxy_handler = ProxyHandler({
    'http': '127.0.0.1:1080',
    'https': '127.0.0.1:1080'
})
opener = build_opener(proxy_handler)


def queryFrom_SSR_SHARE():
    url = 'https://t.me/s/gyjclub'
    response = opener.open(url)

    html = response.read().decode('utf-8').replace("\\\"", "").replace("\\r", "").replace("\\n", "").replace("\\t",
                                                                                                             "").replace(
        "\\/", "/").replace("/\"", "\"")
    html = BeautifulSoup(html, 'html5lib')
    itemList = html.find_all("div", class_="tgme_widget_message_text js-message_text")

    to_test_urls = []

    for item in itemList:
        ssrHtml = item.get_text().strip()
        if ssrHtml.startswith("ss"):
            to_test_urls.append(ssrHtml)

    return to_test_urls


def queryFrom_youneed1():
    url = 'https://www.youneed.win/free-ssr'
    response = opener.open(url)

    html = response.read().decode('utf-8').replace("\\\"", "").replace("\\r", "").replace("\\n", "").replace("\\t",
                                                                                                             "").replace(
        "\\/", "/").replace("/\"", "\"")
    html = BeautifulSoup(html, 'html5lib')
    itemList = html.find_all("a", string=re.compile('右键复制链接'))

    to_test_urls = []

    for item in itemList:
        ssrHtml = item['href']
        if ssrHtml.startswith("ss"):
            to_test_urls.append(ssrHtml)

    return to_test_urls


def queryFrom_youneed2():
    url = 'https://www.youneed.win/free-ssr/2'
    response = opener.open(url)

    html = response.read().decode('utf-8').replace("\\\"", "").replace("\\r", "").replace("\\n", "").replace("\\t",
                                                                                                             "").replace(
        "\\/", "/").replace("/\"", "\"")
    html = BeautifulSoup(html, 'html5lib')
    itemList = html.find_all("a", string=re.compile('右键复制链接'))

    to_test_urls = []

    for item in itemList:
        ssrHtml = item['href']
        if ssrHtml.startswith("ss"):
            to_test_urls.append(ssrHtml)

    return to_test_urls

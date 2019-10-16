import logging
from urllib.request import ProxyHandler, build_opener

from bs4 import BeautifulSoup

logging.basicConfig(level=logging.INFO)

headers = {
    'Host': 'https://t.me',
    'Referer': 'https://t.me',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
}


def queryFrom_SSR_SHARE():
    url = 'https://t.me/s/gyjclub'
    proxy_handler = ProxyHandler({
        'http': '127.0.0.1:1080',
        'https': '127.0.0.1:1080'
    })
    opener = build_opener(proxy_handler)
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

    print('to_test_urls=', to_test_urls)
    return to_test_urls

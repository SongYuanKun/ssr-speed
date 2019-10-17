import logging
import re

import requests
from bs4 import BeautifulSoup

logging.basicConfig(level=logging.INFO)

proxy_handler = {
    'http': '127.0.0.1:1081',
    'https': '127.0.0.1:1081'
}


def queryFrom_SSR_SHARE():
    url = 'https://t.me/s/gyjclub'

    headers = {
        'Host': 't.me',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Cookie': '_ga=GA1.2.1088835183.1570852098; _gid=GA1.2.369184814.1571203202; stel_ssid=8ac98d52465c9f8e20_15762411972854688158',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
    }

    to_test_urls = []
    try:
        response = requests.get(url, headers=headers, proxies=proxy_handler, timeout=2)

        html = response.content.decode('utf-8').replace("\\\"", "").replace("\\r", "").replace("\\n", "").replace("\\t",
                                                                                                                  "").replace(
            "\\/", "/").replace("/\"", "\"")
        html = BeautifulSoup(html, 'html5lib')
        item_list = html.find_all("a", string=re.compile('右键复制链接'))
        for item in item_list:
            ssr_html = item['href']
            if ssr_html.startswith("ss"):
                to_test_urls.append(ssr_html)
    except Exception as e:
        logging.error("SSR_SHARE请求失败", e)

    return to_test_urls


def queryFrom_youneed1():
    url = 'https://www.youneed.win/free-ssr'
    headers = {
        'referer': 'https://www.youneed.win/free-ssr',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
    }

    to_test_urls = []
    try:
        response = requests.get(url, headers=headers, proxies=proxy_handler, timeout=2)

        html = response.content.decode('utf-8').replace("\\\"", "").replace("\\r", "").replace("\\n", "").replace("\\t",
                                                                                                                  "").replace(
            "\\/", "/").replace("/\"", "\"")
        html = BeautifulSoup(html, 'html5lib')
        item_list = html.find_all("a", string=re.compile('右键复制链接'))
        for item in item_list:
            ssr_html = item['href']
            if ssr_html.startswith("ss"):
                to_test_urls.append(ssr_html)
    except Exception as e:
        logging.error("youneed.win1请求失败", e)

    return to_test_urls


def queryFrom_youneed2():
    url = 'https://www.youneed.win/free-ssr/2'
    headers = {
        'referer': 'https://www.youneed.win/free-ssr',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
    }

    to_test_urls = []
    try:
        response = requests.get(url, headers=headers, proxies=proxy_handler, timeout=2)

        html = response.content.decode('utf-8').replace("\\\"", "").replace("\\r", "").replace("\\n", "").replace("\\t",
                                                                                                                  "").replace(
            "\\/", "/").replace("/\"", "\"")
        html = BeautifulSoup(html, 'html5lib')
        item_list = html.find_all("a", string=re.compile('右键复制链接'))
        for item in item_list:
            ssr_html = item['href']
            if ssr_html.startswith("ss"):
                to_test_urls.append(ssr_html)
    except Exception as e:
        logging.error("youneed.win2请求失败", e)

    return to_test_urls

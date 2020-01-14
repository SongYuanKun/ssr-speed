import logging

import requests

from foo import html_util

logging.basicConfig(level=logging.INFO)


def get_from_ssrjiedian():
    url = 'https://www.ssrjiedian.com/'
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (bindows NT 10.0; bin64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
    }
    to_test_urls = []
    try:
        response = requests.get(url, headers=headers, proxies=html_util.proxy_handler, timeout=2)
        html = html_util.format_response(response)
        item_list = html.find_all("p")
        list1 = []
        for item in item_list:
            list1.extend(item.get_text().split(','))
        for item4 in list1:
            if item4.startswith("ss"):
                to_test_urls.append(item4)
    except Exception as e:
        logging.error("ssrjiedian请求失败", e)
    return to_test_urls

import logging

import requests

from foo import html_util

logging.basicConfig(level=logging.INFO)

headers = {
    'Host': 't.me',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*; \
                  q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (bindows NT 10.0; bin64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
                    Chrome/77.0.3865.90 Safari/537.36'
}


def query(url):
    to_test_urls = []
    try:
        response = requests.get(url, headers=headers, proxies=html_util.proxy_handler, timeout=2)
        html = html_util.format_response(response)
        requests.session().close()
        item_list = html.find_all("div", class_="tgme_widget_message_text js-message_text")
        list1 = []
        for item in item_list:
            list1.extend(item.get_text().split(','))
        for item4 in list1:
            if item4.startswith("ss"):
                to_test_urls.append(item4)
    except Exception as e:
        logging.error(url + "请求失败", e)
        requests.session().close()
    return to_test_urls


def get_from_1():
    url = 'https://t.me/s/ssrshares'
    return query(url)


def get_from_2():
    url = 'https://t.me/s/freeshadowsock'
    return query(url)


def get_from_3():
    url = 'https://t.me/s/lRANSSR'
    to_test_urls = []
    return query(url)


def get_from_4():
    url = 'https://t.me/s/SSRSUB'
    return query(url)


def get_from_5():
    url = 'https://t.me/s/gudaocesu'
    return query(url)


def get_from_6():
    url = 'https://t.me/s/ssr_v2'
    return query(url)


def get_from_7():
    url = 'https://t.me/s/jcfabu'
    return query(url)


def get_from_8():
    url = 'https://t.me/s/FreeSSRNode'
    return query(url)


def get_from_9():
    url = 'https://t.me/s/vpn_lulula'
    return query(url)


def get_from_10():
    url = 'https://t.me/s/woyaofq'
    return query(url)


if __name__ == '__main__':
    print(get_from_4())

import logging

import pyperclip
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

from foo import my_chrome_driver

logging.basicConfig(level=logging.INFO)

proxy_handler = {
    'http': '127.0.0.1:1081',
    'https': '127.0.0.1:1081'
}


def get_from_ssr_share():
    url = 'https://t.me/s/ssrshares'
    headers = {
        'Host': 't.me',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (bindows NT 10.0; bin64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
    }
    to_test_urls = []
    try:
        response = requests.get(url, headers=headers, proxies=proxy_handler, timeout=2)
        html = format_response(response)
        item_list = html.find_all("div", class_="tgme_widget_message_text js-message_text")
        for item in item_list:
            ssr_html = item.get_text().strip()
            if ssr_html.startswith("ss"):
                to_test_urls.append(ssr_html)
    except Exception as e:
        logging.error("SSR_SHARE请求失败", e)

    return to_test_urls


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
        response = requests.get(url, headers=headers, proxies=proxy_handler, timeout=2)
        html = format_response(response)
        item_list = html.find_all("p")
        list1 = []
        list2 = []
        list3 = []
        list4 = []
        for item in item_list:
            list1.extend(item.get_text().split(','))
        for item1 in list1:
            list2.extend(item1.split('</br>'))
        for item2 in list2:
            list3.extend(item2.split('\\n'))
        for item3 in list3:
            list4.extend(item3.split('\n'))
        for item4 in list4:
            if item4.startswith("ss"):
                to_test_urls.append(item4)
    except Exception as e:
        logging.error("ssrjiedian请求失败", e)
    return to_test_urls


def get_from_SSRSUB():
    url = 'https://t.me/s/SSRSUB'
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
        response = requests.get(url, headers=headers, proxies=proxy_handler, timeout=2)
        html = format_response(response)
        item_list = html.find_all("div", class_="tgme_widget_message_text js-message_text")
        list1 = []
        list2 = []
        list3 = []
        list4 = []
        for item in item_list:
            list1.extend(item.get_text().split(','))
        for item1 in list1:
            list2.extend(item1.split('</br>'))
        for item2 in list2:
            list3.extend(item2.split('\\n'))
        for item3 in list3:
            list4.extend(item3.split('\n'))
        for item4 in list4:
            if item4.startswith("ss"):
                to_test_urls.append(item4)
    except Exception as e:
        logging.error("SSRSUB请求失败", e)
    return to_test_urls


def get_from_lncn():
    to_test_urls = []
    url = 'https://lncn.org/'
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--proxy-server=http://127.0.0.1:1081')
    chrome_options.add_argument('-no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(executable_path=my_chrome_driver.chrome_driver_path,
                              options=chrome_options)
    driver.get(url)
    driver.implicitly_wait(10)
    try:
        driver.find_elements_by_xpath('//*[@id="app"]/div[2]/div/div[2]/div/div[1]/div[4]/button')[0].click()
        to_test_urls = pyperclip.paste().split(',')
    except Exception as e:
        logging.error("lncn请求失败", e)
    driver.quit()
    return to_test_urls


def format_response(response):
    html = response.content.decode('utf-8') \
        .replace("\\\"", "").replace("\\r", "") \
        .replace("\\n", "").replace("\\t", "") \
        .replace("\\/", "/").replace("/\"", "\"")
    return BeautifulSoup(html, 'html5lib')


if __name__ == "__main__":
    get_from_lncn()

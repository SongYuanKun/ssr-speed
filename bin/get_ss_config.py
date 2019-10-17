import logging

from selenium import webdriver

logging.basicConfig(level=logging.INFO)

proxy_handler = {
    'http': '127.0.0.1:1081',
    'https': '127.0.0.1:1081'
}


def query_from_free_ss():
    url = 'https://free-ss.site/'

    headers = {
        'authority': 'free-ss.site',
        'method': 'GET',
        'path': '/',
        'scheme': 'https',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'no-cache',
        'cookie': '__cfduid=de0eb7b16dff4ce27d20140ce6f0119921571305047; _ga=GA1.2.1642592003.1571305053; _gid=GA1.2.1971631806.1571305053',
        'referer': 'https://www.google.com.hk/',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
    }

    to_test_urls = []
    try:

        service_args = [
            '--proxy=https://127.0.0.1:1081'
            '--proxy-type=https'
        ]
        driver = webdriver.PhantomJS(executable_path='../win/phantomjs.exe', service_args=service_args)
        driver.get(url)
        driver.implicitly_wait(30)
        # 设置30秒页面超时返回，类似于requests.get()的timeout选项，driver.get()没有timeout选项
        driver.set_page_load_timeout(30)
        # 获取网页资源（获取到的是网页所有数据）
        html = driver.page_source
        driver.quit()
        print(html)
    except Exception as e:
        logging.error("free_ss请求失败", e)

    return to_test_urls


if __name__ == '__main__':
    query_from_free_ss()

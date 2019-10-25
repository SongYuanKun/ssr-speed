import logging

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

logging.basicConfig(level=logging.INFO)


def query_from_free_ss():
    url = 'https://free-ss.site/'

    to_test_urls = []
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--proxy-server=http://127.0.0.1:1081')
    # chrome_options.add_argument('--headless')
    # chrome_options.add_argument('--disable-gpu')
    capabilities = DesiredCapabilities.CHROME.copy()
    capabilities['acceptSslCerts'] = True
    capabilities['acceptInsecureCerts'] = True

    driver = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe',
                              options=chrome_options, desired_capabilities=capabilities)
    driver.maximize_window()
    driver.get(url)
    driver.implicitly_wait(10)
    WebDriverWait(driver, 10, 0.5).until(
        expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, '#tbss tbody tr')))
    print(driver.page_source)
    driver.quit()
    return to_test_urls


def get_from_youneed():
    url = 'https://www.youneed.win/free-ss'
    to_test_urls = []
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--proxy-server=http://127.0.0.1:1081')
    chrome_options.add_argument('-no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe',
                              options=chrome_options)
    driver.get(url)
    WebDriverWait(driver, 30, 0.5).until(
        expected_conditions.visibility_of_element_located((By.CLASS_NAME, 'v2ray')))
    html = BeautifulSoup(driver.page_source, 'html5lib')
    driver.quit()
    item_list = html.find_all("table tbody tr")
    for item in item_list:
        ssr_html = item['href']
        if ssr_html.startswith("ss"):
            to_test_urls.append(ssr_html)
    return to_test_urls


if __name__ == '__main__':
    get_from_youneed()

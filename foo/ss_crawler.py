import logging

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from foo import my_chrome_driver

logging.basicConfig(level=logging.INFO)


def query_from_free_ss():
    url = 'https://free-ss.site/'

    to_test_urls = []
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--proxy-server=http://127.0.0.1:1081')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    capabilities = DesiredCapabilities.CHROME.copy()
    capabilities['acceptSslCerts'] = True
    capabilities['acceptInsecureCerts'] = True

    driver = webdriver.Chrome(executable_path=my_chrome_driver.chrome_driver_path,
                              options=chrome_options, desired_capabilities=capabilities)
    driver.get(url)
    driver.implicitly_wait(10)
    WebDriverWait(driver, 30, 1).until(
        expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, '#tbss tbody tr')))
    print(driver.page_source)
    driver.quit()
    return to_test_urls

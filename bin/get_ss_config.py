import logging

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

logging.basicConfig(level=logging.INFO)


def query_from_free_ss():
    # url = 'https://www.baidu.com/'
    url = 'https://free-ss.site/'

    to_test_urls = []
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--proxy=https://127.0.0.1:1081')
    chrome_options.add_argument('--proxy-type=https')
    # chrome_options.add_argument('--headless')
    # chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe',
                              options=chrome_options)
    driver.maximize_window()
    driver.get(url)
    driver.implicitly_wait(10)
    WebDriverWait(driver, 10, 0.5).until(
        expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, '#tbss tbody tr')))
    print(driver.page_source)
    driver.quit()
    return to_test_urls


if __name__ == '__main__':
    query_from_free_ss()
